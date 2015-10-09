from flask import current_app, request, Blueprint, session
from flask.ext.sqlalchemy import SQLAlchemy
from utils import load_config, generate_unique_id, get_random_experiment
from .views import abt, getStats, mostConverts
import yaml
import random

@abt.record
def init_app(state):
    app = state.app

    config = load_config('config.yaml')
    app.config.update(config)
    app.secret_key = 'secret_key'
    app.db = SQLAlchemy(app)

    #TODO: Move models to a models.py to make code look nice
    class Test(app.db.Model):
        __tablename__ = "Test"
        test_id = app.db.Column(app.db.String, primary_key = True)
        name = app.db.Column(app.db.String)
        winner = app.db.Column(app.db.String)

        def __init__(self, test_id, name):
            self.test_id = test_id
            self.name = name
            self.winner = "None"

    class Experiment(app.db.Model):
        __tablename__ = "Experiment"
        experiment_id = app.db.Column(app.db.Integer, primary_key = True)
        test_id = app.db.Column(app.db.String)
        experiment = app.db.Column(app.db.String)
        participation = app.db.Column(app.db.Integer)
        convert = app.db.Column(app.db.Integer)

        def __init__(self, test_id, experiment):
            self.test_id = test_id
            self.experiment = experiment
            self.participation = 0
            self.convert = 0

    app.db.create_all()
    add_url_rules(Test, Experiment)

    #when test is called in a jinja template
    def test(test_name, *experiments):
        test = Test.query.filter_by(name = test_name).first()

        if test == None:
            test_id = generate_unique_id()
            test = Test(test_id,test_name)
            for exp in experiments:
                experiment = Experiment(test_id, exp)
                app.db.session.add(experiment)
            app.db.session.add(test)
            app.db.session.commit()

        experiment = get_random_experiment(Experiment, test.test_id)
        experiment.participation = experiment.participation + 1
        app.db.session.commit()
        _begin_experiment(test.test_id, experiment.experiment)
        return experiment.experiment

    #when converted is called in a jinja template
    def converted(test_name):
        test = Test.query.filter_by(name = test_name).first()
        experiment = _get_session().get(test.test_id,None)
        if experiment != None:
            exp = Experiment.query.filter_by(test_id = test.test_id, experiment=experiment).first()
            exp.convert = exp.convert + 1
            app.db.session.commit()
            _get_session().pop(test.test_id, None)
        return ""

    #set the jinja global template variables
    app.jinja_env.globals.update({
        'test':test,
        'converted': converted
    })

#store current running test in a session
def _get_session():
    if 'abt' not in session:
        session['abt'] = {}
    return session['abt']

def _begin_experiment(test_id,experiment_name):
    _get_session()[test_id] = experiment_name
    session.modified = True

def add_url_rules(Test, Experiment):
    def convertRateWrapper():
        return mostConverts(Test, Experiment)

    def getStatsWrapper():
        return getStats(Test, Experiment)

    abt.add_url_rule('/getStats', 'getStatsWrapper', getStatsWrapper)
    abt.add_url_rule('/convertRate', 'convertRateWrapper', convertRateWrapper)



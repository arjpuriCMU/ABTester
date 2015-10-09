import os
from flask import Flask, Blueprint, jsonify, request, render_template, redirect, url_for, flash, jsonify
from flask.ext.sqlalchemy import SQLAlchemy

root = os.path.abspath(os.path.dirname(__file__))
abt = Blueprint('abt', __name__,
    template_folder=os.path.join(root, 'templates'),
    static_folder=os.path.join(root, 'static'),
    url_prefix='/abt'
)

@abt.route('/')
def index():
    return 'insert beautiful UI here'

def getStats(Test, Experiment):
    result = {'tests' : []}
    for test in Test.query.all():
        test_res = {'test_name' : test.name, 'experiments': []}
        experiments = Experiment.query.filter_by(test_id = test.test_id).all()
        for exp in experiments:
            if exp.convert > 0.0:
                convert_rate =((exp.convert*1.0)/exp.participation)*100
            else:
                convert_rate = "inf"
            test_res['experiments'].append({'experiment': exp.experiment, 'participation': exp.participation, 'converts': exp.convert, 'convert_rate': convert_rate})

        result['tests'].append(test_res)
    return jsonify(result)


def mostConverts(Test, Experiment):
    result = {'tests' : []}
    for test in Test.query.all():
        test_res = {'test name' : test.name, 'winner': None, 'max convert rate': 0}
        experiments = Experiment.query.filter_by(test_id = test.test_id).all()
        max_convert_rate = 0.0
        best_exp_res = {}
        for exp in experiments:
            if exp.convert > 0.0:
                convert_rate =((exp.convert*1.0)/exp.participation)*100
            else:
                continue
            if convert_rate > max_convert_rate:
                max_convert_rate = convert_rate
                best_exp_res = {'experiment': exp.experiment, 'participation': exp.participation, 'converts': exp.convert, 'convert_rate': convert_rate}
        test_res['max convert rate'] = max_convert_rate
        test_res['winner'] = best_exp_res
        result['tests'].append(test_res)

    return jsonify(result)





import os
import yaml
import uuid
import random

def load_config(config_fn):
    # Load the specialized template file
    script_dir = os.path.dirname(__file__)
    config_file = os.path.join(script_dir, config_fn)
    return yaml.load(file(config_file))

def generate_unique_id():
    return str(uuid.uuid4())

def get_random_experiment(Experiment, test_id):
    experiments = Experiment.query.filter_by(test_id = test_id).all()
    return random.choice(experiments)

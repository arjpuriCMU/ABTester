from flask import Flask, Blueprint, jsonify, request, render_template, redirect, url_for, flash
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)


root = os.path.abspath(os.path.dirname(__file__))
abt = Blueprint('abt', 'flask.ext.split',
    template_folder=os.path.join(root, 'templates'),
    static_folder=os.path.join(root, 'static'),
    url_prefix='/abt'
)

@abt.route('/')
def index():
    k
    index_temp = 'index.html'
    return render_template(index_temp)


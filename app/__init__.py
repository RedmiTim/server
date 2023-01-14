import os
import sys

from flask import Flask
from flask.cli import load_dotenv
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from .islands import blueprint as islands

sys.path.insert(0, os.path.dirname(__file__))

load_dotenv('.env')

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URI')
app.register_blueprint(islands)

db = SQLAlchemy(app)
migrate = Migrate(app, db)


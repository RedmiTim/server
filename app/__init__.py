import os
import sys

from flask import Flask
from flask.cli import load_dotenv
from flask_migrate import Migrate
from .islands import blueprint as islands
from .tables import db
from .users import blueprint as users

sys.path.insert(0, os.path.dirname(__file__))

load_dotenv('.env')

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URI')
db.init_app(app)
migrate = Migrate(app, db, compare_type=True)
app.config['db'] = db
app.register_blueprint(islands)
app.register_blueprint(users)


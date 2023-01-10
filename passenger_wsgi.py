import os
import sys
from flask import Flask
import migrations
import islands.routes
from exceptions.types import EntityNotFoundError
from database import load
from os import environ
import dotenv

sys.path.insert(0, os.path.dirname(__file__))

dotenv.load_dotenv('variables.env')
load(environ)
migrations.migrate()

application = Flask(__name__)
application.register_blueprint(islands.routes.blueprint)


@application.errorhandler(404)
@application.errorhandler(EntityNotFoundError)
def not_found(_):
    return 'Not found', 404
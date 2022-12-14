import flask
import migrations
import islands.routes
from exceptions.types import EntityNotFoundError
from database import load
from os import environ
import dotenv


dotenv.load_dotenv('variables.env')
load(environ)
migrations.migrate()

app = flask.Flask(__name__)
app.register_blueprint(islands.routes.blueprint)


@app.errorhandler(404)
@app.errorhandler(EntityNotFoundError)
def not_found(_):
    return 'Not found', 404


app.run(debug=True)

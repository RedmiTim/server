import flask
import migrations

migrations.migrate()

app = flask.Flask(__name__)

app.run(debug=True)
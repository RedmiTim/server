import flask
import migrations
import islands.routes

migrations.migrate()

app = flask.Flask(__name__)
app.register_blueprint(islands.routes.blueprint)

app.run(debug=True)

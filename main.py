import random
import storage
import flask
app = flask.Flask(__name__)


def user():
    id0 = random.randint(1, 1000000)
    id = str(id0)
    name = flask.request.data.decode()
    enter_in_file = storage.create_user(name, id)
    return 'Юзер создан'


app.add_url_rule('/user', view_func=user, methods=['POST'])
app.run(debug=True)
# привет от Карима
# и от хасанова

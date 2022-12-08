import random
import storage
l=random.randint(1,1000000)
b=str(l)
d=input('Введите никнейм')
s=storage.create_user(d,b)
import flask
app = flask.Flask(__name__)
def user():
    name = flask.request.args['a']
    k=storage.create_user(name)
    return 'Вы передали: ' + name
app.add_url_rule('/user', view_func=user)
app.run(debug=True)
# привет от Карима
# и от хасанова
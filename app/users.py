from flask import Blueprint, request, current_app

from app.defaults import start_island
from app.tables import user, island, unit

blueprint = Blueprint('users', __name__)


@blueprint.post('/')
def create_user():
    db = current_app.config['db']
    user_id = db.session.execute(user.insert().values(nickname=request.json['nickname'])).inserted_primary_key[0]
    island_id = db.session.execute(
        island.insert().values(user_id=user_id, map_id=start_island['map_id'])).inserted_primary_key[0]
    db.session.execute(
        unit.insert(),
        list(map(lambda un: {
            'island_id': island_id,
            'x': un['x'], 'y': un['y'],
            'name': un['name']
        }, start_island['units'])))
    db.session.commit()
    return {'status': 'created', 'id': str(user_id)}, 201, {'Location': '/' + str(user_id)}


@blueprint.get('/<user_id>')
def get_user(user_id):
    db = current_app.config['db']
    result = db.session.execute(db.select([user.c.nickname, user.c.id]).where(user.c.id == user_id)).first()
    if result is None:
        return 'User not found', 404
    return {
        'id': result.id,
        'nickname': result.nickname
    }

from flask import Blueprint, current_app
from sqlalchemy import and_
from sqlalchemy.sql import exists

from app.tables import user, island, unit

blueprint = Blueprint('islands', __name__)


def map_islands(db, cursor, user_id):
    return list(map(lambda i:
                    {'id': i.id,
                     'map_id': i.map_id,
                     'units': list(
                         map(lambda un: {'x': un.x, 'y': un.y},
                             db.session.execute(
                                 unit.select().where(and_(unit.c.user_id == user_id, unit.c.island_id == i.id))))
                     )}, cursor))


@blueprint.get('/<user_id>/islands')
def get_user_islands_ids(user_id):
    db = current_app.config['db']
    u_id = int(user_id)
    if not db.session.query(exists(user.select().where(user.c.id == u_id))).scalar():
        return 'User not found', 404
    result = db.session.execute(db.select([island.c.id]).where(island.c.user_id == u_id)).all()
    return list(map(lambda i: i.id, result))


@blueprint.get('/<user_id>/islands/attackable')
def get_attackable_islands_ids(user_id):
    db = current_app.config['db']
    u_id = int(user_id)
    if not db.session.query(exists(user.select().where(user.c.id == u_id))).scalar():
        return 'User not found', 404
    result = db.session.execute(db.select([island.c.id]).where(island.c.user_id != u_id)).all()
    return list(map(lambda i: i.id, result))


@blueprint.get('/islands/<island_id>')
def get_island(island_id):
    db = current_app.config['db']
    result = db.session.execute(island.select().where(island.c.id == island_id)).first()
    if result is None:
        return 'Island not found', 404
    return {
        'map_id': result.map_id,
        'units': list(
            map(lambda un: {'name': un.name, 'x': un.x, 'y': un.y},
                db.session.execute(
                    unit.select().where(and_(unit.c.island_id == island_id))))
        )}


@blueprint.put('/<user_id>/islands/<island_id>')
def update_island(user_id, island_id):
    pass
    # new_user_id, new_island_id = islands.storage.update_island(int(user_id), int(island_id), request.json)
    # return 'island updated', 204, {'Location': f'/{new_user_id}/islands/{new_island_id}'}

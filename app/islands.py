from datetime import datetime, time, timedelta

from flask import Blueprint, current_app, request
from sqlalchemy import and_, or_
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
    db.session.execute(island.update().where(island.c.attacked_on > datetime.now() - timedelta(minutes=15))
                       .values(attacked_on=None))
    u_id = int(user_id)
    if not db.session.query(exists(user.select().where(user.c.id == u_id))).scalar():
        return 'User not found', 404
    result = db.session.execute(db.select([island.c.id])
                                .where(and_(island.c.user_id != u_id, island.c.id.is_(None)))).all()
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


@blueprint.put('/islands/<island_id>')
def attack_island(island_id):
    db = current_app.config['db']
    i_id = int(island_id)
    if not db.session.query(exists(island.select().where(island.c.id == i_id))).scalar():
        return 'Island not found', 404
    db.session.execute(island.update().where(island.c.id == i_id).values(attacked_on=datetime.now()))
    db.session.commit()
    return 'You have 15 minutes to concuest it', 202


@blueprint.post('/islands/<island_id>')
def finish_attack(island_id):
    db = current_app.config['db']
    i_id = int(island_id)
    if not db.session.query(exists(island.select().where(island.c.id == i_id))).scalar():
        return 'Island not found', 404
    db.session.execute(island.update().where(island.c.id == i_id).values(attacked_on=None))
    if 'winner' in request.json.keys():
        db.session.execute(island.update().where(island.c.id == i_id).values(user_id=request.json['winner']))
    db.session.execute(unit.delete().where(unit.c.island_id == i_id))
    db.session.execute(
        unit.insert(),
        list(map(lambda un: {
            'island_id': island_id,
            'x': un['x'], 'y': un['y'],
            'name': un['name']
        }, request.json['units'])))
    db.session.commit()
    return 'Applied', 200

from flask import Blueprint, request
import storage

blueprint = Blueprint('/islands', __name__)


@blueprint.post('/')
def create_user_islands():
    return 'islands created', 201


@blueprint.get('/')
def get_user_islands():
    return storage.get_user_islands(int(request.args['userid'])), 200, {'Content-Type': 'application/json'}


@blueprint.get('/attackable')
def get_attackable_islands():
    return storage.get_attackable_islands(int(request.args['userid'])), 200, {'Content-Type': 'application/json'}

from flask import Blueprint

blueprint = Blueprint('islands', __name__)


@blueprint.get('/')
def test():
    return 'test'


@blueprint.post('/<user_id>/islands')
def create_user_islands(user_id):
    # islands.storage.create_user_islands(int(user_id))
    return 'islands created', 201


@blueprint.get('/<user_id>/islands')
def get_user_islands(user_id):
    pass
    # return islands.storage.get_user_islands(int(user_id))


@blueprint.get('/<user_id>/islands/attackable')
def get_attackable_islands(user_id):
    pass
    # return islands.storage.get_attackable_islands(int(user_id))


@blueprint.get('/<user_id>/islands/<island_id>')
def get_island(user_id, island_id):
    pass
    # return islands.storage.get_island(int(user_id), int(island_id))


@blueprint.put('/<user_id>/islands/<island_id>')
def update_island(user_id, island_id):
    pass
    # new_user_id, new_island_id = islands.storage.update_island(int(user_id), int(island_id), request.json)
    # return 'island updated', 204, {'Location': f'/{new_user_id}/islands/{new_island_id}'}

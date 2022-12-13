from database import connect
from exceptions.types import EntityNotFoundError
from islands.defaults import start_island


def create_unit(db, user_id, island_id, unit: dict):
    query = f'''INSERT INTO island_units (island_id, user_id, x, y, name, health) VALUES 
    ({island_id}, {user_id}, {unit['x']}, {unit['y']}, "{unit['name']}", {unit['health'] if 'health' in unit.keys() else 'NULL'})'''
    db.execute(query)


def create_user_islands(user_id):
    with connect() as db:
        create_island = f'INSERT INTO islands (id, user_id, map_id) VALUES (1, {user_id}, {start_island["map_id"]})'
        db.execute(create_island)
        for unit in start_island['units']:
            create_unit(db, user_id, 1, unit)


def get_user_islands(user_id):
    query = f'SELECT id FROM islands WHERE user_id={user_id}'
    with connect() as db:
        return [n[0] for n in db.execute(query).fetchall()]


def get_attackable_islands(user_id):
    query = f'''
    SELECT user_id AS 'usid', id FROM islands 
    WHERE user_id != {user_id}
    ORDER BY (SELECT COUNT (*) FROM islands WHERE user_id=usid) 
    LIMIT 10
    '''
    with connect() as db:
        return [{'user_id': n[0], 'id': n[1]} for n in db.execute(query).fetchall()]


def get_island(user_id, island_id):
    get_map_id = f'SELECT map_id FROM islands WHERE user_id={user_id} AND id={island_id}'
    get_units = f'''
    SELECT x, y, name, health FROM island_units 
    WHERE user_id={user_id} AND island_id={island_id}
    '''

    def map_unit(unit):
        r = {'x': unit[0], 'y': unit[1], 'name': unit[2]}
        if unit[3] is not None:
            r['health'] = unit[3]
        return r

    with connect() as db:
        if db.execute(f'SELECT COUNT(*) FROM islands WHERE user_id={user_id} AND id={island_id}').fetchall()[0][0] == 0:
            raise EntityNotFoundError
        return {
            'map_id': db.execute(get_map_id).fetchall()[0][0],
            'units': [map_unit(n) for n in db.execute(get_units).fetchall()]
        }


def update_island(old_user_id, old_island_id, island):
    with connect() as db:
        if db.execute(f'SELECT COUNT(*) FROM islands WHERE user_id={old_user_id} AND id={old_island_id}') \
                .fetchall()[0][0] == 0:
            raise EntityNotFoundError
        new_id = db.execute(f'SELECT MAX(id) FROM islands WHERE user_id={island["user_id"]}').fetchall()[0][0] + 1
        update = f'''
        UPDATE islands
        SET user_id={island['user_id']}, id={new_id}
        WHERE user_id={old_user_id} AND id={old_island_id}
        '''
        db.execute(update)
        for unit in island['units']:
            create_unit(db, island['user_id'], new_id, unit)
        return island["user_id"], new_id

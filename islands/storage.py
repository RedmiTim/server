from database import connect


def create_user_islands(user_id):
    query = '''
    INSERT INTO islands (id, user_id, units_json) VALUES (
    1,
    ''' + user_id + ''',
    '
    {"units":[{"name":"tank","type":"land","weapons":["medium"],"health":10,"speed":1,"rotation_speed":0.5},{"name":"rocket_launcher","texture":"truck","type":"land","weapons":["rocket_launcher"],"health":5,"speed":0.8,"rotation_speed":0.3},{"name":"ship_defence","texture":"dot","type":"building","weapons":["ship_defence"],"health":15},{"name":"air_defence","texture":"dot","type":"building","weapons":["air_rocket_launcher"],"health":15},{"name":"transport_ship","type":"big_ship","weapons":[{"name":"ship","location":{"x":1,"y":0}},{"name":"ship","location":{"x":2,"y":0}}],"health":100,"speed":1,"rotation_speed":0.1,"min_damage":10},{"name":"bomber","type":"plane","health":10,"speed":3,"rotation_speed":0.1,"bomb_count":4,"bomb":{"texture":"bomb","power":15,"range":1.5}},{"name":"landing_craft","type":"small_ship","health":10,"speed":1,"rotation_speed":0.1,"weapons":[]}],"weapons":[{"name":"medium","reload":2,"range":6,"rotation_speed":0.8,"bullet_starts":[{"x":0,"y":0}],"bullet":{"name":"standard","damage":2,"speed":5,"flight_height":1,"target_height":1,"bang":false,"creation_sound":"shot"}},{"name":"rocket_launcher","reload":4,"range":11,"rotation_speed":0.2,"bullet_starts":[{"x":0,"y":0}],"bullet":{"name":"rocket","damage":10,"speed":2,"flight_height":3,"target_height":1,"bang":true,"bang_range":0.8,"creation_sound":"rocket_start"}},{"name":"air_rocket_launcher","reload":4,"range":11,"rotation_speed":0.5,"bullet_starts":[{"x":0,"y":0}],"bullet":{"name":"rocket","damage":10,"speed":4,"flight_height":4,"target_height":4,"bang":false,"creation_sound":"rocket_start"}},{"name":"ship_defence","reload":6,"range":10,"rotation_speed":0.3,"bullet_starts":[{"x":0,"y":0}],"bullet":{"name":"standard","damage":10,"speed":7,"flight_height":1,"target_height":1,"bang":false,"creation_sound":"shot"}},{"name":"ship","reload":5,"range":10,"rotation_speed":0.1,"bullet_starts":[{"x":0,"y":0.2},{"x":0,"y":-0.2}],"bullet":{"name":"standard","damage":5,"speed":7,"flight_height":2,"target_height":1,"bang":false,"creation_sound":"shot"}}],"graphics":[{"name":"bang","lifetime":3,"next":"pit","spawn_sound":"bang"},{"name":"pit","lifetime":120},{"name":"big_bang","lifetime":3,"next":"big_pit","spawn_sound":"bang"},{"name":"big_pit","lifetime":120},{"name":"hit","lifetime":1,"spawn_sound":"hit"}]}
    '
    )
    '''
    with connect() as db:
        db.execute(query)


def _query_islands(query):
    with connect() as db:
        return '[' + ','.join(n[0] for n in db.execute(query).fetchall()) + ']'


def get_user_islands(user_id):
    query = f'SELECT (units_json) FROM islands WHERE user_id={user_id}'
    return _query_islands(query)


def get_attackable_islands(user_id):
    query = f'''
    SELECT (units_json, user_id as usid) FROM islands 
    WHERE usid != {user_id}
    ORDER BY (SELECT COUNT (*) FROM ISLANDS WHERE user_id=usid) 
    LIMIT 10
    '''
    return _query_islands(query)

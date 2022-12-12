from database import connect


def get_user_islands(user_id):
    with connect() as db:
        for island in db.execute(f'SELECT (units_json) FROM islands WHERE user_id={user_id}').fetchall():
            return island


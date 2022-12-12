from database import connect


migrations = [
    '''
    CREATE TABLE MIGRATIONS(
        version INT NOT NULL PRIMARY KEY
    )
    ''',
    '''
    CREATE TABLE islands(
        user_id INT NOT NULL,
        id INT NOT NULL,
        units_json VARCHAR NOT NULL,
        PRIMARY KEY (user_id, id)
    )
    ''',
]


def migrate():
    with connect() as db:
        max_migration = db.execute('SELECT MAX(version) FROM migrations').fetchall()
        print(max_migration)

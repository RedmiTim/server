import sqlite3

from database import connect

migrations = [
    '''
    CREATE TABLE migrations(
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
    'ALTER TABLE islands DROP COLUMN units_json',
    '',
    '''
    CREATE TABLE island_units(
        island_id INT NOT NULL,
        x INT NOT NULL,
        y INT NOT NULL,
        health INT
    )
    ''',
    'ALTER TABLE islands ADD COLUMN map_id INTEGER NOT NULL',
    'ALTER TABLE island_units ADD COLUMN user_id INTEGER NOT NULL',
    'ALTER TABLE island_units ADD COLUMN name VARCHAR NOT NULL',
]



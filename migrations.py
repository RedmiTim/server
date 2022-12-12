import sqlite3
import mysql.connector

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
    '''
]


def migrate():
    with connect() as db:
        try:
            current_migration = int(db.execute('SELECT MAX(version) FROM migrations').fetchall()[0][0]) + 1
        except sqlite3.OperationalError:
            current_migration = 0
        except mysql.connector.DatabaseError:
            current_migration = 0
        for migration_version in range(current_migration, len(migrations)):
            db.execute(migrations[migration_version])
            db.execute(f'INSERT INTO migrations VALUES({migration_version})')

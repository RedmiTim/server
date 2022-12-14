import sqlite3
import mysql.connector


db_type = ''
host = ''
database = ''
user = ''
password = ''


def load(env):
    global db_type, host, database, user, password
    db_type = env.get('DATABASE_TYPE')
    host = env.get('DATABASE_HOST')
    database = env.get('DATABASE')
    user = env.get('DATABASE_USER')
    password = env.get('DATABASE_PASSWORD')


def connect():
    if db_type == 'mysql':
        return mysql.connector.connect(host=host, database=database, user=user, password=password)
    elif db_type == 'sqlite':
        return sqlite3.connect(database)
    print(f'ERROR: Unknown database type: {db_type}')


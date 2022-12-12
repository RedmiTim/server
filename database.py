import sqlite3
import mysql.connector

db_type = 'sqlite'
host = ''
database = 'localdatabase.db'
user = ''
password = ''


def connect():
    if db_type == 'mysql':
        return mysql.connector.connect(host=host, database=database, user=user, password=password)
    elif db_type == 'sqlite':
        return sqlite3.connect(database)
    print(f'ERROR: Unknown database type: {db_type}')


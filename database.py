from sqlite3 import connect as connect_lite
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
        return connect_lite(database)
    print(f'ERROR: Unknown database type: {db_type}')

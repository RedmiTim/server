from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, ForeignKey, String

db = SQLAlchemy()

user = db.Table(
    'user',
    Column('id', Integer, nullable=False, primary_key=True),
    Column('nickname', String, nullable=False)
)

island = db.Table(
    'island',
    Column('user_id', Integer, ForeignKey('user.id'), nullable=False, primary_key=True),
    Column('id', Integer, nullable=False, primary_key=True),
    Column('map_id', Integer, nullable=False),
)

unit = db.Table(
    'island_units',
    Column('island_id', Integer, ForeignKey('island.id'), nullable=False),
    Column('user_id', Integer, ForeignKey('user.id'), nullable=False),
    Column('x', Integer, nullable=False),
    Column('y', Integer, nullable=False),
    Column('health', Integer),
)
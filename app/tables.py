from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, ForeignKey, String, DateTime

db = SQLAlchemy()

user = db.Table(
    'user',
    Column('id', Integer, nullable=False, primary_key=True),
    Column('nickname', String(100), nullable=False)
)

island = db.Table(
    'island',
    Column('id', Integer, nullable=False, primary_key=True),
    Column('user_id', Integer, ForeignKey('user.id'), nullable=False),
    Column('map_id', Integer, nullable=False),
    Column('attacked_on', DateTime)
)

unit = db.Table(
    'unit',
    Column('island_id', Integer, ForeignKey('island.id'), nullable=False),
    Column('name', String(length=50), nullable=False),
    Column('x', Integer, nullable=False),
    Column('y', Integer, nullable=False),
    Column('health', Integer),
)

from sqlalchemy import Column, Integer, ForeignKey, String

from app import db

db.Table(
    'user',
    Column('id', Integer, nullable=False, primary_key=True),
    Column('nickname', String, nullable=False)
)

db.Table(
    'island',
    Column('user_id', Integer, ForeignKey('user.id'), nullable=False, primary_key=True),
    Column('id', Integer, nullable=False, primary_key=True),
)

db.Table(
    'island_units',
    Column('island_id', Integer, ForeignKey('island.id'), nullable=False),
    Column('user_id', Integer, ForeignKey('island.user.id'), nullable=False),
    Column('x', Integer, nullable=False),
    Column('y', Integer, nullable=False),
    Column('health', Integer),
)
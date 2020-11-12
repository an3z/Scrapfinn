from sqlalchemy import create_engine, Column, Table, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import (Integer, Text, SmallInteger, DateTime, TIMESTAMP, String, Date, Float, Boolean, Text, LargeBinary, VARCHAR)
from datetime import datetime
from scrapy.utils.project import get_project_settings

Base = declarative_base()

def db_connect():
    """
    Performs database connection using database settings from settings.py.
    Returns sqlalchemy engine instance
    """
    return create_engine(get_project_settings().get("CONNECTION_STRING"))

def create_table(engine):
    Base.metadata.create_all(engine)

class finnboligDB(Base):
    __tablename__ = "finnbolig"

    id = Column(Integer, primary_key=True)
    finn_code = Column('finn_code', Integer)
    address = Column('address', VARCHAR(255))
    total_price = Column('total_price', Integer)
    common_costs = Column('common_costs', VARCHAR(255))
    for_sale_price = Column('for_sale_price', Integer)
    ownership_form = Column('ownership_form', VARCHAR(255))
    building_type = Column('building_type', VARCHAR(255))
    bedrooms = Column('bedrooms', Integer)
    pra = Column('pra', Integer)
    year_built = Column('year_built',  SmallInteger)
    last_changed = Column('last_changed', VARCHAR(255))
    rooms = Column('rooms', SmallInteger)
    timestamp = Column(TIMESTAMP(timezone=False), nullable=False, default=datetime.now())


class NewboligDB(Base):
    __tablename__ = "newbolig"

    id = Column(Integer, primary_key=True)
    finn_code = Column('finn_code', Integer)
    address = Column('address', VARCHAR(255))
    total_price = Column('total_price', Integer)
    common_costs = Column('common_costs', VARCHAR(255))
    for_sale_price = Column('for_sale_price', Integer)
    bedrooms = Column('bedrooms', Integer)
    pra = Column('pra', Integer)
    last_changed = Column('last_changed', VARCHAR(255))
    rooms = Column('rooms', SmallInteger)
    timestamp = Column(TIMESTAMP(timezone=False), nullable=False, default=datetime.now())


class ParkingDB(Base):
    __tablename__ = "parking"

    id = Column(Integer, primary_key=True)
    finn_code = Column('finn_code', VARCHAR(255))
    title = Column('title', VARCHAR(255))
    headline = Column('headline', VARCHAR(255))
    address = Column('address', VARCHAR(255))
    price = Column('price', VARCHAR(255))
    timestamp = Column(TIMESTAMP(timezone=False), nullable=False, default=datetime.now())



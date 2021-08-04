from sqlalchemy import (
    Column,
    Date,
    ForeignKey,
    Integer,
    Numeric,
    String,
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from database import engine

Base = declarative_base()

class Bot(Base):
	__tablename__ = "bot"
	id = Column(Integer, primary_key=True)

class User(Base):
	__tablename__ = "user"
	id = Column(Integer, primary_key=True)


Base.metadata.create_all(engine)
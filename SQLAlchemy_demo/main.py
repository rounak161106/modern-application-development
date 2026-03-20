from sqlalchemy import create_engine                              # for connecting our app to the database
from sqlalchemy import Table, Integer, String, ForeignKey, Column # For creation of database
from sqlalchemy import select                                     # for fetching data from the database

from sqlalchemy.orm import relationship 
from sqlalchemy.orm import declarative_base 
from sqlalchemy.orm import Session

Base = declarative_base()

class Author(Base):
    __tablename__ = "Authors"
    id = Column(Integer, autoincrement=True, primary_key=True)
    name = Column(String, unique=True)
    email = Column(String, unique=True)

class Article(Base):
    __tablename__ = "Articles"
    id = Column(Integer, autoincrement=True, primary_key=True)
    name = Column(String, unique=True)
    email = Column(String, unique=True)

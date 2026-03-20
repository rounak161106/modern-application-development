from sqlalchemy import create_engine                              # for connecting our app to the database
from sqlalchemy import Table, Integer, String, ForeignKey, Column # For creation of database
from sqlalchemy import select                                     # for fetching data from the database

from sqlalchemy.orm import relationship 
from sqlalchemy.orm import declarative_base 
from sqlalchemy.orm import Session

Base = declarative_base()

class Author(Base):
    __tablename__ = "authors"
    author_id = Column(Integer, autoincrement=True, primary_key=True)
    name = Column(String, unique=True)
    email = Column(String, unique=True)

class Article(Base):
    __tablename__ = "articles"
    article_id = Column(Integer, autoincrement=True, primary_key=True)
    title = Column(String)
    content = Column(String)
    authors = relationship("Author", secondary="article_authors")

class ArticleAuthor(Base):
    __tablename__ = "article_authors"
    author_id = Column(Integer, ForeignKey("authors.author_id"), primary_key=True, nullable=False)
    article_id = Column(Integer, ForeignKey("articles.article_id"), primary_key=True, nullable=False)

engine = create_engine("sqlite:///testdb.sqlite3")
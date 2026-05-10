"""
main.py — Raw SQLAlchemy Demo (Without Flask)
===============================================
Practice: Learning SQLAlchemy ORM independently of Flask

This was my first time using SQLAlchemy directly — without Flask-SQLAlchemy.
The goal was to understand the ORM layer on its own:
    - How to create an engine and connect to a database
    - How to define models using declarative_base()
    - How to create sessions for database operations
    - How transactions work (commit vs rollback)
    - How Many-to-Many relationships work through association tables

This understanding was essential before moving to Flask-SQLAlchemy,
which wraps SQLAlchemy with Flask-specific conveniences.

Key concepts learned:
    - create_engine() — establishes database connection
    - declarative_base() — base class for ORM models
    - Session — manages database transactions
    - relationship() with secondary — Many-to-Many relationships
    - Transaction handling with try/except and commit/rollback
    - select() for querying data
"""

# ──────────────────────────────────────────────────────────
# Imports
# ──────────────────────────────────────────────────────────
from sqlalchemy import create_engine                              # for connecting our app to the database
from sqlalchemy import Table, Integer, String, ForeignKey, Column # For creation of database
from sqlalchemy import select                                     # for fetching data from the database

from sqlalchemy.orm import relationship 
from sqlalchemy.orm import declarative_base 
from sqlalchemy.orm import Session

# ──────────────────────────────────────────────────────────
# Models — using raw SQLAlchemy (no Flask)
# ──────────────────────────────────────────────────────────
# declarative_base() creates a base class that our models inherit from.
# This is the raw SQLAlchemy way — Flask-SQLAlchemy replaces this with db.Model.
Base = declarative_base()

class Author(Base):
    """Represents an author who can write articles."""
    __tablename__ = "authors"
    author_id = Column(Integer, autoincrement=True, primary_key=True)
    name = Column(String, unique=True)
    email = Column(String, unique=True)

class Article(Base):
    """Represents an article that can have multiple authors."""
    __tablename__ = "articles"
    article_id = Column(Integer, autoincrement=True, primary_key=True)
    title = Column(String)
    content = Column(String)
    # Many-to-Many: an article can have many authors, an author can write many articles
    authors = relationship("Author", secondary="article_authors")

class ArticleAuthor(Base):
    """Junction table for the Many-to-Many relationship between Article and Author."""
    __tablename__ = "article_authors"
    author_id = Column(Integer, ForeignKey("authors.author_id"), primary_key=True, nullable=False)
    article_id = Column(Integer, ForeignKey("articles.article_id"), primary_key=True, nullable=False)

# ──────────────────────────────────────────────────────────
# Database Engine
# ──────────────────────────────────────────────────────────
# create_engine() creates a connection to the SQLite database
engine = create_engine("sqlite:///./SQLAlchemy_demo/testdb.sqlite3")


# ──────────────────────────────────────────────────────────
# Example 1: Basic Querying (commented out — learning progression)
# ──────────────────────────────────────────────────────────
# This was my first attempt at querying — using select() and Session
# if __name__ == "__main__":
#     stmt = select(Author)
#     print(stmt)
#     with engine.connect() as conn:
#         for row in conn.execute(stmt):
#             print(row)

#     # find the author name who are related with article id 1
#     with Session(engine) as session:
#         articles = session.query(Article).filter(Article.article_id == 1).all()
#         for article in articles:
#             print(article.title)
#             for author in article.authors:
#                 print(author.name)


# ──────────────────────────────────────────────────────────
# Example 2: Transaction Handling (commented out — learning progression)
# ──────────────────────────────────────────────────────────
# Here I learned about transactions — how to commit or rollback
# if something goes wrong during a series of database operations
# if __name__ == "__main__":
#     with Session(engine, autoflush=False) as session:
#         session.begin()
#         try:
#             article = Article(title = "Dummy article", content = "This is dummy content")
#             session.add(article)
#             session.flush()
#             # raise Exception("Dummy error")
#             article_author = ArticleAuthor(author_id = 1, article_id = article.article_id)
#             session.add(article_author)
#         except:
#             print("Rolling Back")
#             session.rollback()
#             raise
#         else:
#             print("Commit")
#             session.commit()


# ──────────────────────────────────────────────────────────
# Example 3: Using Relationships (active — final learning stage)
# ──────────────────────────────────────────────────────────
# This is the cleanest approach — using relationship() to automatically
# handle the junction table instead of manually creating ArticleAuthor rows
if __name__ == "__main__":
    with Session(engine, autoflush=False) as session:
        session.begin()
        try:
            # Query existing authors
            author1 = session.query(Author).filter(Author.name == "Rounak").one()
            author2 = session.query(Author).filter(Author.name == "Rajesh").one()
            # Create a new article
            article = Article(title = "This is new content using relationship", content = "Hello")
            # Append authors using the relationship — SQLAlchemy automatically
            # creates the corresponding rows in the article_authors junction table
            article.authors.append(author1)
            article.authors.append(author2)
            session.add(article)
        except:
            print("Rolling Back")
            session.rollback()
            raise
        else:
            print("Commit")
            session.commit()

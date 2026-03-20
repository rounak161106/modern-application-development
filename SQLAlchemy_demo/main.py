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

engine = create_engine("sqlite:///./SQLAlchemy_demo/testdb.sqlite3")


# Basic querying
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


# Transaction Handling
if __name__ == "__main__":
    with Session(engine, autoflush=False) as session:
        session.begin()
        try:
            article = Article(title = "Dummy article", content = "This is dummy content")
            session.add(article)
            session.flush()
            # raise Exception("Dummy error")
            article_author = ArticleAuthor(author_id = 1, article_id = article.article_id)
            session.add(article_author)
        except:
            print("Rolling Back")
            session.rollback()
            raise
        else:
            print("Commit")
            session.commit()
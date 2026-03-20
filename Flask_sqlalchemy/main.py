from flask import Flask, request, render_template
from flask_sqlalchemy import SQLAlchemy

import os
path = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + os.path.join(path, "testdb.sqlite3")
db = SQLAlchemy()
db.init_app(app)
app.app_context().push()

class Author(db.Model):
    __tablename__ = "authors"
    author_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    name = db.Column(db.String, unique=True)
    email = db.Column(db.String, unique=True)

class Article(db.Model):
    __tablename__ = "articles"
    article_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    title = db.Column(db.String)
    content = db.Column(db.String)
    authors = db.relationship("Author", secondary="article_authors")

class ArticleAuthor(db.Model):
    __tablename__ = "article_authors"
    author_id = db.Column(db.Integer, db.ForeignKey("authors.author_id"), primary_key=True, nullable=False)
    article_id = db.Column(db.Integer, db.ForeignKey("articles.article_id"), primary_key=True, nullable=False)

@app.route('/')
def main():
    articles = Article.query.all() #or db.session.query(Article).all()
    return render_template("index.html", articles= articles)

@app.route("/article_by/<user_name>")
def article_by(user_name):
    articles = Article.query.filter(Article.authors.any(name = user_name))
    return render_template("article_by.html", articles = articles)

if __name__ == "__main__":
    app.run(debug=True)
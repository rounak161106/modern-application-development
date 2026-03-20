from flask import Flask, request, render_template, redirect
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import Session

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
    return render_template("article_by.html", articles = articles, author = user_name)

@app.route("/create", methods=["GET"])
def create():
    return render_template("create.html")

@app.route("/create_author", methods=["GET"])
def create_author():
    return render_template("create_author.html")


@app.route("/add", methods=["POST"])
def add():
    author_id = request.form.get("author")
    title = request.form.get("title")
    content = request.form.get("content")
    # 1. Get author from DB
    author = Author.query.get(author_id)

    if not author:
        return "Author not found"

    # 2. Create new article
    new_article = Article(title=title, content=content)

    # 3. Link author (this auto handles article_authors table)
    new_article.authors.append(author)

    # 4. Save to DB
    db.session.add(new_article)
    db.session.commit()

    return redirect("/")

@app.route("/add_author", methods=["POST"])
def add_author():
    name = request.form.get("author")
    email = request.form.get("title")
    new_author = Author(name=name, email=email)
    db.session.add(new_author)
    db.session.commit()
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)
from flask_restful import Resource, Api
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///testdb.sqlite3"

db = SQLAlchemy(app)

app.app_context().push()

api = Api(app)

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

class UserApi(Resource):
    def get(self, username):
        print(username)
        user_obj = Author.query.filter_by(name = username).first()
        return {
            "username" : user_obj.name,
            "email" : user_obj.email
            }, 200

    def put(self, username):
        pass
    
    def delete(self, username):
        pass

    def push(self):
        pass

api.add_resource(UserApi, "/api/user" , "/api/user/<string:username>")

if __name__ == "__main__":
    app.run(debug=True)
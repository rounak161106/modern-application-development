from flask_restful import Resource, Api, fields, marshal_with
from flask import Flask, make_response
from flask_sqlalchemy import SQLAlchemy
from werkzeug.exceptions import HTTPException    #to handle exceptions

class NotFoundError(HTTPException):
    def __init__(self, status_code):
        self.response = make_response('', status_code)

output_fields = {
    "author_id" : fields.Integer, 
    "name" : fields.String, 
    "email" : fields.String
} #write all the fields which you want to return as a response

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
    @marshal_with(output_fields)
    def get(self, username):
        print(username)
        user_obj = Author.query.filter_by(name = username).first()
        if user_obj:
            return user_obj
        else:
            # return {"Message" : "User not found"}, 404
            raise NotFoundError(status_code=404)

    def put(self, username):
        pass
    
    def delete(self, username):
        pass

    def push(self):
        pass

api.add_resource(UserApi, "/api/user" , "/api/user/<string:username>")

if __name__ == "__main__":
    app.run(debug=True)
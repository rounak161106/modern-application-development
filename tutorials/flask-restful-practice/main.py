from flask_restful import Resource, Api, fields, marshal_with, reqparse
from flask import Flask, make_response, request
from flask_sqlalchemy import SQLAlchemy
import json
from werkzeug.exceptions import HTTPException    #to handle exceptions

class NotFoundError(HTTPException):
    def __init__(self, status_code):
        self.response = make_response('', status_code)

class BusinessValidationError(HTTPException):
    def __init__(self, status_code, error_code, error_message):
        message = {"error_code" : error_code, "error_message" : error_message}
        self.response = make_response(json.dumps(message), status_code)

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

create_user_parser = reqparse.RequestParser()
create_user_parser.add_argument('username')
create_user_parser.add_argument('email')

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

    def post(self):
        args = create_user_parser.parse_args()
        name = args.get("username", None) 
        email = args.get("email", None) 

        if not name or not email:
            raise BusinessValidationError(status_code=404, error_code="BE1001", error_message="Shouldn't be none")

        new_user_obj = Author(name = name, email = email)
        db.session.add(new_user_obj)
        db.session.commit()
        return {"Message": "Added"},201

api.add_resource(UserApi, "/api/user" , "/api/user/<string:username>")

if __name__ == "__main__":
    app.run(debug=True)
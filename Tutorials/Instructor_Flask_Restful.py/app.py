from flask import Flask, request
from models import *
from flask_restful import Api, Resource

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///apidb.sqlite3"
db.init_app(app)
api = Api(app)
app.app_context().push()

#Rest api for employee table
class EmployeeApi(Resource):
    def get(self, id):
        emp = db.session.query(Employee).filter(Employee.id == id).first()
        
        if emp:
            return {"id" : emp.id, "name" : emp.name, "city" : emp.city}
        else:
            return {"Message" : "Record is not found"}, 404

    def put(self, id):
        pass
    
    def delete(self, id):
        pass
    
    def post(self):
        data = request.json
        name = data["name"]
        city = data["city"]
        print(data)
        print(name)
        print(city)
        new_emp = Employee(name = name, city = city)
        db.session.add(new_emp)
        db.session.commit()
        return {"Message" : "Record created"}, 201
    
#Api routes
api.add_resource(EmployeeApi, "/api/add", "/api/search/<id>")

if __name__ == "__main__":
    app.run(debug=True)
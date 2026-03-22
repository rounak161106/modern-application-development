from flask import Flask ,request
app = Flask(__name__)

data = [
    {"name":"Rounak", "age":18, "marks":90},
    {"name":"Aditya", "age":19, "marks":89},
    {"name":"Chirag", "age":19, "marks":67},
]

@app.route('/get_data')
def get_data():
    return data

@app.route('/student/<name>')
def get_name(name):
    print(request.args.get("name"))
    for i in data:
        if i.get("name") == name:
            return i                                   #sends the response with 200 ok status code
    return {"message": "Student data not found"}, 404  #sends the response with a 404 status code

# The browser provides us a medium only for get method in case of api calls and what about post?? ==> for that we use interfaces like thunderclient, postman(UI) or curl(CLI)

#post methods usage
@app.route('/add', methods=['POST'])   #or we can write @app.post('/add') - only some syntax change
def add_name():
    new_name = request.json
    data.append(new_name)
    return {"message":"Student added successfully"}, 201    #sends the response with 201 status code meaning post is successful and new data is added but the data addes is not persistent and will only be added till that server is running




app.run(debug=True)

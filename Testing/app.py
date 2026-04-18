from flask import Flask, request,jsonify
app = Flask(__name__)
stud_data = [
    {"id":101, "name":"Ram"},
    {"id":102, "name":"Akshay"},
]

@app.route("/")
def get():
    return jsonify(stud_data)

@app.route("/add", methods = ["GET", "POST"])
def add():
    args=request.json
    stud_data.append({"id":args["id"], "name":args["name"]})
    return {"message":"Added successfully"}, 201

app.run(debug=True)
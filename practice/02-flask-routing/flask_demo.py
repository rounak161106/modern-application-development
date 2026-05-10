from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)

@app.route('/', methods=["GET","POST"])
def hello_world():
    if request.method == "GET":
        return render_template('./index.html')
    
    elif request.method == "POST":
        user_name = request.form["name"]
        return render_template('display_details.html', name=user_name)
    
    else:
        print("Something went wrong")

if __name__ == '__main__':
    app.run(debug=True)
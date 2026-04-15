from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)

@app.route('//')
def hello_world():
    return "hello"

@app.route('/search///')
def hellorld():
    return "agda"

if __name__ == '__main__':
    app.run(debug=True)
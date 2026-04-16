from flask import Flask

app = Flask(__name__)

@app.route('//')
def index():
    return "this is index page"
@app.route('/aboutpage')
def Home():
    return 'This is my home page'

@app.route('/projectpage/')
def projects():
    return 'The project page'

@app.route('/aboutpage/projectpage///')
def result():
    return 'This is about the project page'

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
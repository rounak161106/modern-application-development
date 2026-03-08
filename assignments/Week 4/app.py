from flask import Flask
from flask import render_template
from flask import request
import matplotlib

app = Flask(__name__)
# @app.route("/", method=["GET", "POST"])
# def main()




if __name__ == "__main__":
    app.run(debug=True)
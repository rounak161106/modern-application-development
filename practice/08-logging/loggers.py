# This is a simple tutorial to use loggers instead of using print statement to debug our code

from flask import Flask, render_template
import logging
logging.basicConfig(filename="debug.log", level=logging.WARNING)
app = Flask(__name__)
@app.route("/")
def index():
    app.logger.warning("Index page was accessed")
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)
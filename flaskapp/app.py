from flask import Flask
from flask_cors import CORS

app = Flask(__name__)

CORS(app, origins="https://storage.mtls.cloud.google.com/webapp-dlegesse-test/frontend/app.html") 

@app.route("/")
def hello():
    return "Hello, World! This is a simple Flask application."

@app.route("/about")
def about():
    return "This is the about page."

@app.route("/greet/<name>")
def greet(name):
    return f"Hello, {name}!"

if __name__ == "__main__":
    app.run(debug=True, port=8080)

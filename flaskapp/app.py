from flask import Flask

app = Flask(__name__)

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

from flask import Flask

my_app = Flask("My first web app deployment")

@my_app.route('/')

def hello_world():
    return "Hello World"

if __name__ == "main":
    my_app.run(debug=True)
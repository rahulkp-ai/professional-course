from flask import Flask

app = Flask(__name__)
# main server file

@app.route('/')

def hello_world():
    return "<b> My First Application in action ! <br>"
# routing

# to run flask application 
# open terminal in flask app dir
# activate venv
# export flask settings 

'''export FLASK_APP=app.py
export FLASK_ENV=development
export FLASK_DEBUG=1'''

# run flask app
# flask run then go to localhost

def index():
    return {"message": "Hello world"}
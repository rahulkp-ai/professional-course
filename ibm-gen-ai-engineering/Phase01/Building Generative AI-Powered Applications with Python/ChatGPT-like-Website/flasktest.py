from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, world'

@app.route('/loop')
def printLoop():
    result = ""
    for i in range(100):
        # We calculate the number and add it to a string with a line break (<br>)
        calculation = 1 + 10 
        result += f"Loop {i}: The result is {calculation}<br>"
    
    # Send the final built string to the web browser
    return result

if __name__ == '__main__':
    app.run(debug=True)
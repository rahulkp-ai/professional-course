# Import Flask framework
# Flask is the web framework that allows Python to act as a web server
from flask import Flask, render_template

# Import a custom function from another Python file (quotes.py)
# This function returns a random quote from a list
from quotes import get_random_quote


# Create a Flask application instance
# __name__ tells Flask where the application is located
app = Flask(__name__)


# ROUTE DECORATOR
# This tells Flask:
# "When the user visits the root URL (http://127.0.0.1:5000/),
# run the function written below."
@app.route("/")
def home():

    # Call the function from quotes.py
    # This returns one random quote string
    quote = get_random_quote()

    # render_template loads an HTML file from the "templates" folder
    #
    # index.html is the frontend page shown to the user
    #
    # quote=quote means:
    # LEFT SIDE  (quote)  → variable name used inside HTML
    # RIGHT SIDE (quote)  → Python variable created above
    #
    # Flask sends this variable to the HTML template engine (Jinja2)
    #
    # In index.html you can access it like this:
    # {{ quote }}
    #
    # Example HTML:
    # <p>{{ quote }}</p>
    #
    # That means:
    # Python quote → passed to HTML → displayed on webpage
    return render_template("index.html", quote=quote)


# This condition checks:
# "Is this file being run directly by Python?"
#
# If yes → start the Flask development server
if __name__ == "__main__":

    # Start the Flask server
    # debug=True enables:
    # 1. Automatic reload when code changes
    # 2. Detailed error messages in browser
    app.run(debug=True)
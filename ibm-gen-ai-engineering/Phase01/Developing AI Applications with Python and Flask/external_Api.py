from flask import Flask
import requests

app = Flask(__name__)

@app.route("/")
def get_author():
    res = requests.get("https://openlibrary.org/search/authors.json?q=Michael%20Crichton")

    if res.status_code == 200:
        return res.json()

    return {"error": "API request failed"}

if __name__ == "__main__":
    app.run(debug=True, port=8000)
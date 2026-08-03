from flask import Flask, render_template, request
from emotion_detection import emotion_detector

app = Flask(__name__)

@app.route("/")

def home():
    return render_template("index.html")

@app.route("/emotionDetector")

def detect_emotion():
    text_to_analyze = request.args.get("text")
    response = emotion_detector(text_to_analyze)

    return response

if __name__ == "main":
    app.run(debug=True)
from flask import Flask, request, jsonify
from flask_cors import CORS
import json
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer

app = Flask(__name__)
CORS(app)

model_name = "facebook/blenderbot-400M-distill"
print("Loading Blenderbot model...")
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)

# Keep track of history
conversation_history = []

# --- FIX 1: Add a root route so hitting http://127.0.0.1:5000/ shows something ---
@app.route('/', methods=['GET'])
def home():
    return "Flask Chatbot Server is running! Send POST requests to /chatbot."

@app.route('/chatbot', methods=['POST'])
def handle_prompt():
    global conversation_history
    
    data = request.get_data(as_text=True)
    data = json.loads(data)
    input_text = data['prompt']

    # Keep only the last 4 exchanges to prevent token explosion
    conversation_history = conversation_history[-8:]

    # --- FIX 2: Blenderbot expects history separated by its special </s> <s> tags ---
    # We join history with a space, then add the new input
    context = " ".join(conversation_history) + " " + input_text if conversation_history else input_text

    # Tokenize as a single unified string block
    inputs = tokenizer(context, return_tensors="pt", truncation=True, max_length=512)

    # Generate the response
    outputs = model.generate(**inputs, max_new_tokens=60) 

    # Decode the response
    response = tokenizer.decode(outputs[0], skip_special_tokens=True).strip()

    # Add interaction to conversation history
    conversation_history.append(input_text)
    conversation_history.append(response)

    # Returning clean text back to your frontend
    return response

if __name__ == '__main__':
    app.run(port=5000, debug=True)
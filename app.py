from flask import Flask, request, jsonify
import json
import os

app = Flask(__name__)

CACHE_FILE = "../frontend/data/cache.json"

def load_cache():
    if os.path.exists(CACHE_FILE):
        with open(CACHE_FILE,"r") as f:
            return json.load(f)
    return {}

def save_cache(data):
    with open(CACHE_FILE,"w") as f:
        json.dump(data,f)

@app.route("/ask", methods=["POST"])
def ask_ai():

    question = request.json.get("question")

    cache = load_cache()

    if question in cache:
        return jsonify({"answer": cache[question]})

    answer = "AI generated answer for: " + question

    cache[question] = answer
    save_cache(cache)

    return jsonify({"answer": answer})


@app.route("/quiz")
def quiz():
    return jsonify({
        "question":"What is Photosynthesis?",
        "options":[
            "Process plants use to make food",
            "Animal breathing",
            "Earth rotation"
        ],
        "answer":0
    })


if __name__ == "__main__":
    app.run(debug=True)
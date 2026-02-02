from flask import Flask, request, jsonify
from flask_cors import CORS
from memory import get_memory, save_memory
from reasoning import reason_answer
from search import google_search

app = Flask(__name__)
CORS(app)  # 🚨 cho phép frontend gọi API

@app.route("/ask", methods=["POST"])
def ask():
    data = request.get_json(force=True)
    question = data.get("question", "")
    session_id = data.get("session_id", "default")

    memory = get_memory(session_id)

    search_results = google_search(question)
    answer = reason_answer(question, memory, search_results)

    save_memory(session_id, question, answer)

    return jsonify({
        "answer": answer
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

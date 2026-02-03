from flask import Flask, request, jsonify
from flask_cors import CORS
from reasoning import reason_answer

app = Flask(__name__)
CORS(app)

@app.route("/ask", methods=["POST"])
def ask():
    data = request.get_json(force=True)

    question = data.get("question")
    session_id = data.get("session_id")

    if not question:
        return jsonify({"error": "Missing question"}), 400

    answer = reason_answer(question, session_id)

    return jsonify({
        "answer": answer,
        "session_id": session_id
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)

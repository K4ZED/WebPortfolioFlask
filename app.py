import os
from datetime import datetime
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html", name="Kazed", full_name="Kenza Athallah Nandana Wijaya", year=datetime.now().year)


@app.route("/chat", methods=["POST"])
def chat():
    from chatbot import get_response
    data = request.get_json(silent=True) or {}
    message = str(data.get("message", "")).strip()
    if not message or len(message) > 300:
        return jsonify({"response": "Pesan tidak valid."})
    return jsonify({"response": get_response(message)})


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=False)

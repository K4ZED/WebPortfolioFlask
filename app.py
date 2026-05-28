import os
from datetime import datetime
from flask import Flask, render_template, request, jsonify, Response
import urllib.request

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html", name="Kazed", full_name="Kenza Athallah Nandana Wijaya", year=datetime.now().year)


@app.route("/gh-chart")
def gh_chart():
    try:
        req = urllib.request.Request(
            "https://ghchart.rshah.org/39d353/K4ZED",
            headers={"User-Agent": "Mozilla/5.0"}
        )
        with urllib.request.urlopen(req, timeout=6) as r:
            svg = r.read().decode("utf-8")

        # dark mode: dark empty cells + lighter text
        svg = svg.replace("#EEEEEE", "#1e2a1e")
        svg = svg.replace("#767676", "#8b949e")

        return Response(svg, mimetype="image/svg+xml",
                        headers={"Cache-Control": "public, max-age=1800"})
    except Exception:
        return Response('<svg xmlns="http://www.w3.org/2000/svg"/>',
                        mimetype="image/svg+xml")


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

import os
import time
from datetime import datetime
from flask import Flask, render_template, request, jsonify, Response
import urllib.request

app = Flask(__name__)

GH_USER = "K4ZED"
_gh_cache = {"data": None, "ts": 0.0}
_GH_TTL = 1800  # 30 min


@app.route("/")
def home():
    return render_template("index.html", name="Kazed", full_name="Kenza Athallah Nandana Wijaya", year=datetime.now().year)


@app.route("/gh-data")
def gh_data():
    """Proxy GitHub contribution data (date/count/level per day) as JSON, cached in-memory.

    Rendering happens client-side so the calendar can follow the dark/light theme.
    """
    now = time.time()
    if _gh_cache["data"] and now - _gh_cache["ts"] < _GH_TTL:
        return Response(_gh_cache["data"], mimetype="application/json",
                        headers={"Cache-Control": "public, max-age=1800"})
    try:
        req = urllib.request.Request(
            f"https://github-contributions-api.jogruber.de/v4/{GH_USER}?y=last",
            headers={"User-Agent": "Mozilla/5.0"}
        )
        with urllib.request.urlopen(req, timeout=6) as r:
            data = r.read().decode("utf-8")
        _gh_cache["data"] = data
        _gh_cache["ts"] = now
        return Response(data, mimetype="application/json",
                        headers={"Cache-Control": "public, max-age=1800"})
    except Exception:
        # serve stale data on failure, else an empty payload the client can handle
        if _gh_cache["data"]:
            return Response(_gh_cache["data"], mimetype="application/json")
        return Response('{"total":{},"contributions":[]}', mimetype="application/json")


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

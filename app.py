from flask import Flask, render_template, jsonify, request
import json
import os

app = Flask(__name__)

DATA_PATH = os.path.join(os.path.dirname(__file__), "data", "equipment.json")
SWITCHBOARDS_PATH = os.path.join(os.path.dirname(__file__), "data", "switchboards.json")

with open(DATA_PATH, "r", encoding="utf-8") as f:
    EQUIPMENT = json.load(f)

with open(SWITCHBOARDS_PATH, "r", encoding="utf-8") as f:
    SWITCHBOARDS = json.load(f)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/api/search")
def search():
    q = request.args.get("q", "").strip().upper()
    if not q or len(q) < 2:
        return jsonify({"results": [], "query": q})

    results = []
    for item in EQUIPMENT:
        utstyr = item.get("utstyr", "").upper()
        navn = item.get("navn", "").upper()
        tavle = item.get("tavle", "").upper()

        if q in utstyr or q in navn or q in tavle:
            results.append(item)

    results.sort(key=lambda x: (
        0 if x.get("utstyr", "").upper() == q else
        1 if q in x.get("utstyr", "").upper() else 2
    ))

    return jsonify({"results": results[:50], "query": q, "total": len(results)})


@app.route("/api/switchboards")
def switchboards():
    q = request.args.get("q", "").strip().upper()
    if not q or len(q) < 2:
        return jsonify({"results": [], "query": q})

    results = []
    for item in SWITCHBOARDS:
        if (q in item.get("tavle", "").upper()
                or q in item.get("omr", "").upper()
                or q in item.get("beskrivelse", "").upper()
                or q in item.get("mating", "").upper()):
            results.append(item)

    results.sort(key=lambda x: (
        0 if x.get("tavle", "").upper() == q else
        1 if q in x.get("tavle", "").upper() else 2
    ))

    return jsonify({"results": results, "query": q, "total": len(results)})


@app.route("/api/stats")
def stats():
    total = len(EQUIPMENT)
    tavler = len(set(item["tavle"] for item in EQUIPMENT))
    with_utstyr = sum(1 for item in EQUIPMENT if item.get("utstyr"))
    return jsonify({
        "total": total,
        "tavler": tavler,
        "with_utstyr": with_utstyr,
        "switchboards": len(SWITCHBOARDS)
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)

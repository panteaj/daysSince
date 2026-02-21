from flask import Flask, request, jsonify, render_template
from datetime import date
import sqlite3

app = Flask(__name__)

# Database
conn = sqlite3.connect("dates.db", check_same_thread=False)
c = conn.cursor()
c.execute("CREATE TABLE IF NOT EXISTS history(start TEXT,end TEXT,days INT)")
conn.commit()

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/count", methods=["POST"])
def count():
    data = request.json
    start = date.fromisoformat(data["start"])
    end = date.fromisoformat(data["end"])

    days = (end - start).days

    years = end.year - start.year
    months = end.month - start.month

    if end.day < start.day:
        months -= 1
    if months < 0:
        years -= 1
        months += 12

    c.execute("INSERT INTO history VALUES(?,?,?)",(data['start'],data['end'],days))
    conn.commit()

    return jsonify({"days": days,"years": years,"months": months})

@app.route("/age", methods=["POST"])
def age():
    data = request.json
    birth = date.fromisoformat(data["birth"])
    today = date.today()

    years = today.year - birth.year
    months = today.month - birth.month

    if today.day < birth.day:
        months -= 1
    if months < 0:
        years -= 1
        months += 12

    days = (today - birth).days
    return jsonify({"years": years,"months": months,"days": days})

app.run(debug=True)
from flask import Flask, jsonify, render_template, request
import requests

app = Flask(__name__)
import os
from dotenv import load_dotenv

# Load from .env
load_dotenv()

# Use the key
API_KEY = os.getenv("API_KEY")



@app.route("/")
def index():
    return render_template("index.html")

@app.route("/api/countries")
def get_countries():
    r = requests.get(f"{API}/countries")
    return jsonify(r.json())

@app.route("/api/stations")
def get_stations():
    country = request.args.get("country")
    r = requests.get(f"{API}/stations/bycountry/{country}")
    return jsonify(r.json())

if __name__ == "__main__":
    app.run(debug=True)

from flask import Flask, render_template, request, redirect, url_for, jsonify
import json
import requests
from pymongo import MongoClient

app = Flask(__name__)

CONNECTION_STRING = 

def get_database():
    client = MongoClient(CONNECTION_STRING)
    
    return client["SoftwareEngineeringI"]

@app.route("/display-all", methods = ["GET"])
def displayAll():
    db = get_database();
    collection = db["players"]
    players = list(collection.find({}, {"_id": 0}))  # Fetch all players
    print(players)
    players_json = jsonify(players)
    return players_json

if __name__ == "__main__":
    app.run(port = 3000, debug = True)
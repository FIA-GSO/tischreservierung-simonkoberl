import flask
from flask import request, jsonify
import sqlite3

app = flask.Flask(__name__)
app.config["DEBUG"] = True  # Zeigt Fehlerinformationen im Browser, statt nur einer generischen Error-Message


@app.route('/', methods=['GET'])
def home():
    return "<h1>Tischreservierung</h1>"


@app.route("/free_tables", methods=["GET"])
def get_free_tables():

    connect = sqlite3.connect("buchungssystem.sqlite")
    query = "SELECT * FROM reservierungen"
    cur = connect.cursor()
    res = cur.execute(query)
    ret = res.fetchall()

    #Request Parameter abfragen
    if 'zeitpunkt' in request.args:
        wunschzeitpunkt = str(request.args['zeitpunkt'])
        for wunschzeitpunkt in ret:
            pass
    else:
        return "Error: Bitte Zeit Angeben"

    return wunschzeitpunkt


app.run()


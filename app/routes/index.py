from app import app
from flask import Flask, render_template
from pymongo import MongoClient
from json import dumps
import datetime


client = MongoClient('127.0.0.1', 27017)
db = client.customer_analitycs_development

@app.route("/events", methods=['GET', 'POST'])
def events_page():
    result = []
    for ev in db.events.find({}, {'_id': 0}):
        result.append(ev)

    dt_handler = lambda obj: (
        obj.isoformat()
        if isinstance(obj, datetime.datetime)
        or isinstance(obj, datetime.date)
        else None)

    events = dumps(result, default=dt_handler)
    return events



@app.route('/')
def root():
    return app.send_static_file('index.html')

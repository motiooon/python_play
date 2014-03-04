from app import app
from flask import request
from flask.ext.uploads import delete, init, save, Upload
from pymongo import MongoClient
from json import dumps, loads
from faker import Factory
import datetime
import os.path


client = MongoClient('127.0.0.1', 27017)
db = client.people
fake = Factory.create()

@app.route("/people", methods=['GET', 'POST'])
def events_page():

    if request.method == 'POST':
        person = {"author": fake.name(),
                  "text": loads(request.data)['content'],
                  "tags": fake.random_element(array=("mongodb", "python", "pymongo")),
                  "date": datetime.datetime.utcnow()}
        per = db.persons.insert(person)
        return request.data
    else:
        result = []
        for ev in db.persons.find({}, {'_id': 0}):
            result.append(ev)

        dt_handler = lambda obj: (
            obj.isoformat()
            if isinstance(obj, datetime.datetime)
            or isinstance(obj, datetime.date)
            else None)

        ppl = dumps(result, default=dt_handler)
        assert isinstance(ppl, str)
        return ppl

@app.route('/')
def root():
    return app.send_static_file('index.html')


@app.route('/upload', methods=['POST'])
def upload():
    """Upload a new file."""

    def secure_filename(f):
        return f

    def handle_file(f):
        filename = secure_filename(f.filename)
        f.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        return True

    if request.method == 'POST':
        files = request.files.getlist('file')
        for fi in files:
            handle_file(fi)
        return 'ok!'

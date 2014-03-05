from app import app
from flask import request
from flask.ext.uploads import delete, init, save, Upload
from pymongo import MongoClient
from json import dumps, loads
from faker import Factory
import datetime
import os.path
from wand.image import Image
from wand.display import display

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
    """Upload a new file. If file is image then resize one copy and store it in the same folder"""

    def secure_filename(f):
        return f

    def isImage(name):

        extensions = ('.jpg', '.JPG', '.jpeg', '.png')

        for x in extensions:
            if name.endswith(x):
                return True
        return False
    
    def resize(path, w=0.25, h=0.25):
        with Image(filename=path) as img:
            print(img.size)
            with img.clone() as i:
                i.resize(int(i.width * w), int(i.height * h))
                p = path.split("/")
                i.save(filename="/".join([p[0], p[1], '0.25-' + p[2]]))

    def handle_file(f):
        filename = secure_filename(f.filename)
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        f.save(file_path)
        if isImage(file_path):
            resize(file_path)
        return True

    if request.method == 'POST':
        files = request.files.getlist('file')
        for fi in files:
            handle_file(fi)
        return 'ok!'

from domain import web, submission
from repo import local, twilio

from flask import Flask, jsonify, render_template, request, send_from_directory
from flask_cors import CORS
import inspect
from collections import defaultdict
from os import path, environ
import json
from glob import glob

APP_ROOT = path.dirname(path.abspath(__file__))
UPLOAD_FOLDER = path.join(APP_ROOT, 'static/uploads')
SUBMISSION_FOLDER = path.join(APP_ROOT, 'static/submissions')
CALLS = defaultdict(lambda: 0)
ROUTES = [
    'upload',
    'submit',
    'retrieve_submissions',
    'retrieve_upload',
    'health'
]

app = application = Flask('motionandvibration', static_url_path='/static')
CORS(app)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['SUBMISSION_FOLDER'] = SUBMISSION_FOLDER
app.config['MAX_SUBMISSIONS'] = 3

repo = local.Repo(SUBMISSION_FOLDER)

notifier = twilio.Notifier(
    environ['TWILIO_CLIENT_NUMBER'],
    environ['ALERTS_PHONE_NUMBERS'],
    environ['TWILIO_ACCOUNT_SID'],
    environ['TWILIO_AUTH_TOKEN'])



def track_request(route):
    CALLS[route] += 1


@app.route('/uploads', methods=['POST'])
def upload():
    track_request(inspect.stack()[0][3])
    f = request.files['file']
    f.save(path.join(app.config['UPLOAD_FOLDER'], f.filename.replace(" ", "_")))
    return '', 204


@app.route('/uploads/<string:filename>', methods=['GET'])
def retrieve_upload(filename):
    track_request(inspect.stack()[0][3])
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename), 200


@app.route('/submissions', methods=['POST'])
def submit():
    track_request(inspect.stack()[0][3])
    if request.is_json:
        e = submission.Entry(request.get_json()).__validate__()
        repo.__save__(json.dumps(e.data), e.get_id())
        notifier.__notify__(e.get_notification())
        return '', 204
    else:
        return jsonify(web.Error('JSON payload missing')
                       .__tojson__()), 400


@app.route('/submissions', methods=['GET'])
def retrieve_submissions():
    track_request(inspect.stack()[0][3])
    submissions = list()
    for f in glob(app.config['SUBMISSION_FOLDER'] + '/*.json'):
        print(f)
        with open(f, 'r') as fo:
            submissions.append(json.load(fo))
    return jsonify(submissions), 200


@app.route('/health', methods=['GET'])
def health():
    track_request(inspect.stack()[0][3])
    return jsonify(web.Health(CALLS, ROUTES, 'healthy')
                   .__tojson__()), 200


if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask, jsonify, render_template, request
import inspect
from collections import defaultdict
from os import path

from domain import web, submission

APP_ROOT = path.dirname(path.abspath(__file__))
UPLOAD_FOLDER = path.join(APP_ROOT, 'static/uploads')
CALLS = defaultdict(lambda: 0)
ROUTES = [
    'upload',
    'submit',
    'health'
]

app = application = Flask('motionandvibration', static_url_path='')

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_SUBMISSIONS'] = 3


def track_request(route):
    CALLS[route] += 1


@app.route('/upload', methods=['POST'])
def upload():
    track_request(inspect.stack()[0][3])
    f = request.files['file']
    f.save(path.join(app.config['UPLOAD_FOLDER'], f.filename))
    return '', 200


@app.route('/submit', methods=['POST'])
def submit():
    track_request(inspect.stack()[0][3])
    if request.is_json:
        return jsonify(submission.Entry(request.get_json())
                       .__validate__()
                       .__save__()
                       .__notify__()
                       .__tojson__()), 201
    else:
        return jsonify(web.Error('JSON payload missing')
                       .__tojson__()), 400


@app.route('/health', methods=['GET'])
def health():
    track_request(inspect.stack()[0][3])
    return jsonify(web.Health(CALLS, ROUTES, 'healthy')
                   .__tojson__()), 200


if __name__ == '__main__':
    app.run(debug=True)

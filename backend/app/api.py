from flask import Flask, jsonify, render_template, request
from requests import get
import inspect
from collections import defaultdict
from flask_dropzone import Dropzone
import os

APP_ROOT = os.path.dirname(os.path.abspath(__file__))
UPLOAD_FOLDER = os.path.join(APP_ROOT, 'static/uploads')

app = application = Flask("motionandvibration", static_url_path='')

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_SUBMISSIONS'] = 3
app.config['DROPZONE_MAX_FILE_SIZE'] = 10
app.config['DROPZONE_ALLOWED_FILE_CUSTOM'] = True
app.config['DROPZONE_ALLOWED_FILE_TYPE'] = 'audio/*, video/*'
app.config['DROPZONE_DEFAULT_MESSAGE'] = 'drop files or click here'
dropzone = Dropzone(app)
calls = defaultdict(lambda: 0)
remote_ips = defaultdict(lambda: 0)

@app.route("/", methods=["GET"])
def index():
    calls[inspect.stack()[0][3]] += 1
    remote_ip = request.remote_addr if request.remote_addr != '127.0.0.1' else ''
    location = get('http://freegeoip.net/json/' + remote_ip).json()
    print(location)
    return render_template('index.html'), 200


@app.route("/uploadz", methods=["POST"])
def uploadz():
    calls[inspect.stack()[0][3]] += 1
    if remote_ips[request.remote_addr] <= app.config['MAX_SUBMISSIONS']:
        remote_ips[request.remote_addr] += 1
        f = request.files['file']
        f.save(os.path.join(app.config["UPLOAD_FOLDER"], f.filename))
        return "", 200
    else:
        return jsonify({
            "error": "Slow down there cowboy! You only get " + str(app.config['MAX_SUBMISSIONS']) + " submissions. Contact us if you have any questions"
        }), 400


@app.route("/healthz", methods=["GET"])
def healthz():
    calls[inspect.stack()[0][3]] += 1
    return Health(calls) \
               .to_json(), 200


class Health(object):
    def __init__(self, calls):
        self.calls = calls

    def to_json(self):
        return jsonify({
            "requestsServed": {
                "index": self.calls["index"],
                "uploadz": self.calls["uploadz"],
                "healthz": self.calls["healthz"]
            },
            "status": "healthy"
        })


if __name__ == '__main__':
    app.run(debug=True)

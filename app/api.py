from flask import Flask, jsonify, render_template, request
import inspect
from collections import defaultdict
from flask_dropzone import Dropzone
import os

app = application = Flask("motionandvibration", static_url_path='')
APP_ROOT = os.path.dirname(os.path.abspath(__file__))
UPLOAD_FOLDER = os.path.join(APP_ROOT, 'static/uploads')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
dropzone = Dropzone(app)
calls = defaultdict(lambda: 0)


@app.route("/", methods=["GET"])
def index():
    calls[inspect.stack()[0][3]] += 1
    return render_template('index.html'), 200


@app.route("/uploadz", methods=["POST"])
def uploadz():
    calls[inspect.stack()[0][3]] += 1
    f = request.files['file']
    print("**************")
    print(f)
    print(f.filename)
    f.save(os.path.join(app.config["UPLOAD_FOLDER"],f.filename))


    return "", 200


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

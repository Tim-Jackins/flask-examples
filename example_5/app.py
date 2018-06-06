from flask import Flask
from flask import render_template, send_from_directory, url_for
import os
import requests
from time import sleep
from math import sqrt

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/stream_sqrt', methods=['GET'])
def stream():
    def generate():
        for i in range(50):
            yield '{0}\n'.format(round(sqrt(i), 3))
            sleep(1)
    return app.response_class(generate(), mimetype='text/plain')

@app.route('/favicon.ico/')
def favicon():
	return send_from_directory(os.path.join(app.root_path, 'static'), 'favicon.ico',mimetype='image/vnd.microsoft.icon')

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=80)
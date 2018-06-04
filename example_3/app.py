from flask import Flask
from flask import render_template, redirect, url_for
from flask import request, send_file, safe_join, send_from_directory
import os
import requests
import time

app = Flask(__name__)

@app.route('/') # This is the default path for the website (eg www.example.com/)
def start_page():
	return render_template('index.html')

@app.route('/', methods=['POST'])
def my_form_post():
    text = request.form['text']
    processed_text = text.upper()
    return processed_text

@app.route('/input/<string>/') # This is a different path for the website (eg www.example.com/input/word/)
def get_info(string):
	return render_template('info_page.html', secret=string)

@app.route('/favicon.ico/')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'), 'favicon.ico',mimetype='image/vnd.microsoft.icon')

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=80)
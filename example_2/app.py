from flask import Flask, render_template, send_file, safe_join, send_from_directory
import os

app = Flask(__name__)

@app.route('/')
def start_page():
	return render_template('index.html')

@app.route('/secret/')
def send():
	filename = 'secret.txt'
	filepath = 'static/'
	return send_file(filename_or_fp=safe_join(filepath, filename),\
					mimetype='application/octet-stream',\
					as_attachment=True,\
					attachment_filename=filename)	

@app.route('/favicon.ico/')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'), 'favicon.ico',mimetype='image/vnd.microsoft.icon') # This sends the favicon to the browser

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=80)
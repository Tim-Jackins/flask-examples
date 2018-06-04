from flask import Flask, render_template

app = Flask(__name__)

@app.route('/') # This is the default path for the website (eg http://0.0.0.0/)
def start_page(): # The name of the function doesn't really matter
	return render_template('index.html') # Serves up an .html file

@app.route('/other/') # This is a different path for the website (eg http://0.0.0.0/other/)
def other_page():
	return render_template('other_page.html')

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=80)
from flask_socketio import SocketIO, emit
from flask import Flask, render_template, url_for, copy_current_request_context
from random import random
from time import sleep, time
from threading import Thread, Event

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
app.config['DEBUG'] = True

#turn the flask app into a socketio app
socketio = SocketIO(app)

#random number Generator Thread
thread = Thread()
thread_stop_event = Event()

class example_thread(Thread):
	def __init__(self):
		self.delay = 1
		super(example_thread, self).__init__()
	def timeSinceEpoch(self):
		print("Making random numbers")
		while not thread_stop_event.isSet():
			number = str(time())
			socketio.emit('newnumber', {'number': number}, namespace='/data')
			sleep(self.delay)
	def run(self):
		self.timeSinceEpoch()

@app.route('/')
def index():
	return render_template('index.html')

@socketio.on('connect', namespace='/data')
def test_connect():
	global thread
	print('Client connected')

	if not thread.isAlive():
		print("Starting Thread")
		thread = example_thread()
		thread.start()

@socketio.on('disconnect', namespace='/data')
def test_disconnect():
	print('Client disconnected')

if __name__ == '__main__':
	socketio.run(app, host='127.0.0.1',  port=80,)

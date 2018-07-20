# GPIO Pins - Flask

In the last assignment, we connected our Pi to the internet and used SSH to log into the Pi. We can make things a little fancier by setting our Pi up as a web server. This way, it's not just an internet-connected device, it is actually set up to receive requests from anywhere and serve up data. This is basically how the whole internet works (see detailed graphic below).

![pic](media/preview_002.png)

Try this. Get your Pi online, open a terminal window, and find your Pi's IP address using.

```bash
hostname -I
```

Then go to another computer, open up a web browser, and type in that address into the address bar.

Surprise, surprise, it doesn't work.  That's because you can't just go to any old IP address and expect a connection to be allowed, much less any data to be served in return. Time to learn about super cool framework called flask!

Let's start by opening a terminal and making a folder called `flask`.

```bash
mkdir flask
```

Now, head into that folder and make a file called `app.py` in that directory:

```bash
cd flask
nano app.py
```

With `app.py` open, toss in the following code:

```python
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

app.run(host='0.0.0.0', port=80)
```

(To exit nano type: Ctrl+O then Ctrl+X)

Ok, you have just made your first web app! Let's open a terminal and run this bad boy! Go to the folder where `app.py` is, you should already be there, and run the script. P.S. it will fail.

```bash
python3 app.py
```

We haven't used sudo yet, have we? Sometimes you ask your computer "Hey, do _____" and it says "You're not the boss of me!"  So then you have to tell it "I'm a super user, now do _____." The reasoning for this is as follows: port 80 is the default port for web traffic and the computer won't let just any script use it. Well, you have to say "I'm a super user, now run my script."

```bash
sudo python3 app.py
```

Congrats. You just made a web page. Go to that other computer and type the IP address of your Pi. Bam! The browser on that computer just made a request of your Pi and your Pi served up some data!

We're getting there. Next we want to edit your web app to get information from you as well as send it to you. To do this we are going to import request from flask and edit the `/` route to your flask app. Open up `app.py` and add this.

```python
from flask import Flask, request
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def my_form_post():
    if request.method == 'POST':
        text = request.form['text']
        return text
    else:
        return '''
<form method="POST">
Some text: <input name="text">
<input type="submit">
</form>'''

app.run(host='0.0.0.0', port=80)
```

Now start the script again and go check the result on another computer.

Now to complete the assignment. Your goal is to have this little web server interact with the outside world via GPIO.

I hate to just give you the code, so here is an example of how to control GPIO pins in python and you can figure out how to apply it in order to make your app control and LED. Also have a pinout:

![pinout](media/rpi_zero_header.png)

```python
import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)

GPIO.output(18, GPIO.HIGH)
sleep(3)
GPIO.output(18, GPIO.LOW)
```

Two more things and you're done:

1. Add web controls, this can be done with above text field or [buttons or a select field](https://www.w3schools.com/html/html_form_input_types.asp). Go nuts do something cool!

2. Add second LED.

3. Spice up the web interface somehow with [CSS](https://www.w3schools.com/html/html_css.asp) or [images](https://www.google.com/search?q=images&source=lnms&tbm=isch&sa=X&ved=0ahUKEwil6Z2r667cAhUqtlkKHWWjDRUQ_AUICigB&biw=2349&bih=961).
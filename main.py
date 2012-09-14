from flask import Flask
from flask import render_template
app = Flask(__name__)

# import events list
from models import events
from models import about

@app.route('/')
def hello_world():
    return render_template(
    	'index.html',
    	preamble = about.preamble,
    	events = events.eventlist
    )

if __name__ == "__main__":
    app.run()

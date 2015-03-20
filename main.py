from flask import Flask
from flask import render_template
app = Flask(__name__)

# import events list
from models import events


@app.route('/')
def index():
    return render_template(
        'index.html',
        pastevents=events.pastevents,
        upcomingevents=events.upcomingevents
    )


@app.route('/faq/')
def faq():
    return render_template(
        'faq.html'
    )


@app.route('/about/')
def aboutus():
    return render_template(
        'about.html'
    )


@app.route('/schedule/')
def schedule():
    return render_template(
        'schedule.html',
        pastevents=events.pastevents,
        upcomingevents=events.upcomingevents
    )


@app.route('/materials/')
def materials():
    return render_template('materials.html')


@app.route('/materials/railsworkshop2015/')
def materials_rails_workshop2015():
    return render_template('materials/railsworkshop2015.html')

@app.route('/materials/expressworkshop2014/')
def materials_express_workshop2014():
    return render_template('materials/expressworkshop2014.html')


@app.route('/materials/jsworkshop2014/')
def materials_js_workshop2014():
    return render_template('materials/jsworkshop2014.html')


@app.route('/materials/gitworkshop2014/')
def materials_git_workshop2014():
    return render_template('materials/gitworkshop2014.html')


@app.route('/materials/html5workshop2014/')
def materials_html_workshop2014():
    return render_template('materials/html5workshop2014.html')


@app.route('/materials/sinatra/')
def materials_sinatra():
    return render_template('materials/sinatra.html')


@app.route('/materials/html5_2013/')
def html_2013_workshop():
    return render_template('materials/html5workshop2013.html')


@app.route('/materials/html5_2012/')
def materials_html_workshop():
    return render_template('materials/html5workshop.html')


@app.route('/materials/gitjquery/')
def materials_gitjquery():
    return render_template('materials/gitjquery.html')


if __name__ == "__main__":
    app.run()

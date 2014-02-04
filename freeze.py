from flask_frozen import Freezer
from shutil import rmtree
from main import app

app.config['FREEZER_BASE_URL'] = 'http://school.nushackers.org/'

freezer = Freezer(app)

if __name__ == '__main__':
    rmtree('./build', ignore_errors=True)
    freezer.freeze()

import os
from flask_frozen import Freezer
from shutil import rmtree
from main import app

app.config['FREEZER_BASE_URL'] = 'http://school.nushackers.org/'

freezer = Freezer(app)

PATH_TO_MATERIALS = './templates/materials'

@freezer.register_generator
def material_details():
    """
    Need this to keep the material_details route in sync with freeze
    http://pythonhosted.org/Frozen-Flask/#url-generators
    """
    for filename in os.listdir(PATH_TO_MATERIALS):
        if filename.endswith('.html'):
            yield {'material': filename[:-len('.html')]}


if __name__ == '__main__':
    rmtree('./build', ignore_errors=True)
    freezer.freeze()

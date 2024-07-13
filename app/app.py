import random
from flask import jsonify, redirect
from project import create_app
from project.remote import get_images

url = 'https://smashedr.github.io/random-image/'
images = {
    'aviation': []
}

app = create_app()

with app.app_context():
    app.logger.info('app.debug: %s', app.debug)
    app.logger.debug('app.config: %s', app.config)
    for key, value in images.items():
        path = url + key
        app.logger.debug('path: %s', path)
        value.extend(get_images(path))
    app.logger.debug('images: %s', images)


@app.route('/app-health-check')
def flask_health_check():
    return 'success'


@app.route('/')
def index():
    return redirect('https://github.com/smashedr/random-image', code=302)


@app.route('/aviation', strict_slashes=False)
def aviation():
    image = random.choice(images['aviation'])
    app.logger.debug('image: %s', image)
    return redirect(image, code=302)


@app.route('/aviation/images', strict_slashes=False)
def aviation_images():
    app.logger.debug('images: %s', images['aviation'])
    return jsonify(images=images['aviation'])

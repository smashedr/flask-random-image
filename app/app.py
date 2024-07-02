import random
from flask import jsonify, redirect
from project import create_app
from project.remote import get_images

app = create_app()

images = []

with app.app_context():
    app.logger.info('app.debug: %s', app.debug)
    app.logger.debug('app.config: %s', app.config)
    images = get_images(app, images)
    app.logger.debug('images: %s', images)


@app.route('/app-health-check')
def flask_health_check():
    return 'success'


@app.route('/')
def index():
    image = random.choice(images)
    app.logger.debug('image: %s', image)
    return redirect(image, code=302)


@app.route('/images', strict_slashes=False)
def list_images():
    app.logger.debug('images: %s', images)
    return jsonify(images=images)

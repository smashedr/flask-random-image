import re
import requests

url = 'https://smashedr.github.io/random-image'
path = f'{url}/vars.js'


def get_images(app, images):
    if images:
        app.logger.info('----- LOCAL REQUEST -----')
        return images
    else:
        app.logger.info('+++++ REMOTE REQUEST +++++')
        r = requests.get(path)
        pattern = re.compile(r"'([^']*)'")
        images = pattern.findall(r.text)
        images = [f'{url}/{i}' for i in images]
        return images

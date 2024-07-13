import json
import requests


def get_images(path):
    r = requests.get(path + '/images.json')
    images = []
    for image in r.json():
        images.append(path + '/' + image)
    return images

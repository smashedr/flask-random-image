[![Pages](https://github.com/smashedr/flask-random-image/actions/workflows/build.yaml/badge.svg)](https://github.com/smashedr/flask-random-image/actions/workflows/build.yaml)

# Flask Random Image

Flask App to redirect to a random image that can be hosted anywhere or on GitHub Pages.

* Example App/Redirect: https://flask-image.cssnr.com/
* Source Pages: https://smashedr.github.io/random-image/
* Source Repository: https://github.com/smashedr/random-image/

## Notes

This Docker app uses the [build.yaml](.github%2Fworkflows%2Fbuild.yaml) workflow to build images for both amd64
and arm64 architectures using BuildX Bake definitions in the [docker-compose-swarm.yaml](docker-compose-swarm.yaml)
and push them to the GitHub Container Registry.

The sources are currently hard coded in the [remote.py](app%2Fproject%2Fremote.py) file.

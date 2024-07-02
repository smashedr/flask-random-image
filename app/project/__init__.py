from decouple import config
from logging.config import dictConfig
from pathlib import Path

from flask import Flask

dictConfig({
    'version': 1,
    'formatters': {'standard': {
        'format': '[%(asctime)s] %(levelname)s - '
                  '%(module)s.%(funcName)s:%(lineno)d: %(message)s',
    }},
    'handlers': {'console': {
        'class': 'logging.StreamHandler',
        'formatter': 'standard',
    }},
    'loggers': {'root': {
        'level': config('LOG_LEVEL', 'DEBUG'),
        'handlers': ['console'],
        'propagate': config('LOG_PROPAGATE', True, bool),
    }}
})

root_path = Path(__file__).resolve().parent.parent


def create_app():
    app = Flask(__name__, root_path=root_path.absolute().as_posix())

    app.config.from_prefixed_env()

    @app.shell_context_processor
    def ctx():
        return {'app': app}

    return app

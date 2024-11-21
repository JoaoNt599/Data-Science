import os
import logging
from flask import Flask
from app.flaskr.config import db


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='d89bcc337d5c3ee6adc8c84eac8d3063d780f3422eb7c4dc158372090c741087',
        DATABASE=os.path.join('/opt/app/flaskr', 'flaskr.sqlite')
    )

    app.logger.setLevel(logging.DEBUG)

    if test_config is None:
        app.config.from_pyfile("config.py", silent=True)
    else:
        app.config.from_mapping(test_config)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    db.init_app(app)

    from app.flaskr.controllers import home
    from app.flaskr.controllers import comments
    app.register_blueprint(home.bp)
    app.register_blueprint(comments.bp)

    return app

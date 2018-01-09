from flask import Flask
from .models import db
from .views import api_bp


def create_app(config_filename, debug=False):
    app = Flask(__name__)
    app.debug = debug
    app.config.from_object(config_filename)
    db.init_app(app)
    app.register_blueprint(api_bp, url_prefix='/api')
    return app
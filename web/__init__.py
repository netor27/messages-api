from flask import Flask, Blueprint
from flasgger import Swagger
from .models import db
from .views import api_bp

site = Blueprint('site', __name__)

@site.route("/")
def index():
    html = "<h3>Hello world!, this is the index page of the messages-api</h3>"
    return html

def create_app(config_filename, debug=True):
    app = Flask(__name__)
    Swagger(app)
    app.debug = debug
    app.config.from_object(config_filename)
    db.init_app(app)
    app.register_blueprint(site)
    app.register_blueprint(api_bp, url_prefix='/api')
    return app
from flask import Flask, Blueprint

from .views import views
from .api import api_views

def create_app():
    app = Flask(__name__)
    app.secret_key="vitor"
    instantiate_app_blueprints(app)
    return app

def instantiate_app_blueprints(app):
    app.register_blueprint(views, url_prefix="/")
    app.register_blueprint(api_views, name="api", url_prefix="/api")




from flask import Flask, redirect, url_for

from routes.api import api_bp
from routes.fyp import fyp_bp
from routes.profile import profile_bp
from routes.investments import investments_bp
from routes.create_user import create_user_bp


def create_app():
    app = Flask(__name__)

    app.register_blueprint(api_bp)
    app.register_blueprint(fyp_bp)
    app.register_blueprint(profile_bp)
    app.register_blueprint(investments_bp)
    app.register_blueprint(create_user_bp)

    @app.route("/")
    def home():
        return redirect(url_for("create_user.create_user"))
    
    return app



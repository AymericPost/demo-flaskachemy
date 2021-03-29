from flask import Flask, abort
from os import environ

from models import init_db
from controllers.UserController import user_blueprint

def create_app():
    app = Flask(__name__)

    app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://flask:password@localhost/flask_app"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True

    @app.route("/")
    def it_works():
        if(environ["FLASK_ENV"] == "development"):
            return "<h1>It works!</h1>"
        else:
            abort(404)
    
    app.register_blueprint(user_blueprint, url_prefix = "/api/users")
    return init_db(app)
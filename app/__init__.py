from flask import Flask

from environs import Env
from datetime import timedelta

from app.configs import database
from app.configs import migrations
from app.configs import commands
from app.configs import jwt
from app import views

env = Env()
env.read_env()


def create_app():
    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = env('SQLALCHEMY_DATABASE_URI')
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["JSON_SORT_KEYS"] = False
    app.config["JWT_SECRET_KEY"] = env("SECRET_KEY")
    app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(hours=12)
    app.config["JWT_REFRESH_TOKEN_EXPIRES"] = timedelta(days=4)
    app.config["CRIPTOGRAPHY_SECRET_KEY"]= env("CRIPTOGRAPHY_SECRET_KEY")
    database.init_app(app)
    migrations.init_app(app)
    commands.init_app(app)
    jwt.init_app(app)
    views.init_app(app)

    return app

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def init_app(app: Flask) -> None:
    db.init_app(app)
    app.db = db

    from app.models.user_locator_model import UserLocatorModel
    from app.models.car_model import CarModel



from flask import Flask
from flask_migrate import Migrate


def init_app(app: Flask) -> None:

    Migrate(app, app.db, compare_type=True)

    from app.models.user_locator_model import UserLocatorModel
    from app.models.car_model import CarModel

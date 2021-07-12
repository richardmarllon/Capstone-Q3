from app.models.car_model import CarModel
from app.services.helpers import check_incorrect_keys, add_in_db

def post_car_by_data(data) -> tuple:
    required_keys = ["year", "car_plate", "model", "trunk_volume", "insurer", "insurer_number", "review_date", "withdrawal_place", "city", "state", "user_id"]
    check_incorrect_keys(data, required_keys)

    car = CarModel(**data)
    add_in_db(car)
    response = car.serialized()

    return response
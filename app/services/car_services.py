from sqlalchemy.sql.expression import true
from app.models.car_model import CarModel
from app.services.helpers import check_incorrect_keys, add_in_db, format_car_plate, commit_current_session, delete_in_db, format_query_car, format_url_car, check_user, transform_to_uppercase, format_phone_number

def post_car_by_data(data: dict, current_user : dict) -> tuple:
    check_user(data["user_id"], current_user)
    required_keys: list = ["year", "car_plate", "model", "thunk_volume", "insurer", "insurer_number", "review_date", "withdrawal_place", "city", "state", "user_id"]
    check_incorrect_keys(data, required_keys)
    car_plate_to_format = format_car_plate(data)
    insurer_number_to_format = format_phone_number(data)
    
    data["insurer_number"] = insurer_number_to_format
    data["car_plate"] = car_plate_to_format

    data = transform_to_uppercase(data)

    car: CarModel = CarModel(**data)
    add_in_db(car)
    
    return car

def update_car_by_id(car_id: int, data: dict, current_user: dict):
    check_user(data["user_id"], current_user)
    car_plate_to_format = format_car_plate(data)
    insurer_number_to_format = format_phone_number(data)

    data["car_plate"] = car_plate_to_format
    data["insurer_number"] = insurer_number_to_format

    data = transform_to_uppercase(data)
    
    car_to_update = CarModel.query.get(car_id)
    
    for key, value in data.items():
        setattr(car_to_update, key, value)

    commit_current_session()
    
    return car_to_update

def delete_car_by_id(id, current_user): 
    car_to_delete = CarModel.query.get(id)
    if car_to_delete.user_id == current_user['user_id']:
        delete_in_db(car_to_delete)

        return False
    return True
    
def get_car_by_filters(**data):

    year, model, thunk_volume, withdrawal_place, city, state, page, per_page = format_query_car(data)
   

    cars = CarModel.query.filter(
        (CarModel.year==int(year) or True),
        CarModel.model.like(model),
        (CarModel.thunk_volume==int(thunk_volume) or True),
        CarModel.withdrawal_place.like(withdrawal_place),
        CarModel.city.like(city),
        CarModel.state.like(state)).paginate(int(page), int(per_page),error_out=False)

    next_url, prev_url = format_url_car(cars.has_next, cars.has_prev, cars.next_num, cars.prev_num, per_page, data)

    return (cars, next_url, prev_url, cars.total, cars.pages)

def get_car_by_id(id):
    car = CarModel.query.get(id)
    
    return car
from sqlalchemy.sql.expression import true
from app.models.car_model import CarModel
from app.services.helpers import check_incorrect_keys, add_in_db, format_car_plate, commit_current_session, delete_in_db, format_query_car, format_url_car

def post_car_by_data(data: dict) -> tuple:
    required_keys = ["year", "car_plate", "model", "thunk_volume", "insurer", "insurer_number", "review_date", "withdrawal_place", "city", "state", "user_id"]
    check_incorrect_keys(data, required_keys)

    car_plate_to_format = format_car_plate(data)
    data["car_plate"] = car_plate_to_format

    car = CarModel(**data)
    add_in_db(car)
    

    return car

def update_car_by_id(car_id: int, data: dict):

    car_plate_to_format = format_car_plate(data)
    data["car_plate"] = car_plate_to_format
    
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
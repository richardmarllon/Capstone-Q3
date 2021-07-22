from app.exc.not_found_error import NotFound
from app.models.record_lessee_model import RecordLesseeModel
from app.services.helpers import add_in_db, check_incorrect_keys, check_missing_keys, delete_in_db, commit_current_session
from http import HTTPStatus

def post_record_lessee_by_data(data) -> tuple:
    required_keys = ["lessee_id", "car_id", "date"]
    check_incorrect_keys(data, required_keys)
    check_missing_keys(data, required_keys)

    register_lesse = RecordLesseeModel(**data)
    add_in_db(register_lesse)
    response = register_lesse

    return response

def search_record_lessee_by_id(id: int) -> tuple:
    search_result = RecordLesseeModel.query.get(id)

    return search_result


def delete_record_lessee_by_id(id: int):
    register_lesse_to_delete = RecordLesseeModel.query.get(id)

    if not register_lesse_to_delete:
        raise NotFound
    
    delete_in_db(register_lesse_to_delete)
    
    return ""

def update_record_lessee_by_id(id: int, data: dict):
    user_to_update = RecordLesseeModel.query.get(id)

    if not user_to_update:
        raise NotFound
    
    for key, value in data.items():
        setattr(user_to_update, key, value)

    add_in_db(user_to_update)

    return user_to_update
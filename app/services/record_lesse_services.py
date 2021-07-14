from app.models.record_lesse_model import RecordLesseModel
from app.services.helpers import add_in_db, check_incorrect_keys, check_missing_keys, delete_in_db, commit_current_session
from http import HTTPStatus

def post_record_lesse_by_data(data) -> tuple:
    required_keys = ["comment", "lesse_id", "car_id"]
    check_incorrect_keys(data, required_keys)
    check_missing_keys(data, required_keys)

    register_lesse = RecordLesseModel(**data)
    add_in_db(register_lesse)
    response = register_lesse

    return response, HTTPStatus.CREATED

def search_record_lesse_by_id(id: int) -> tuple:
    search_result = RecordLesseModel.query.filter_by.get(id)

    return search_result, HTTPStatus.OK


def delete_record_lesse_by_id(id: int):
    register_lesse_to_delete = RecordLesseModel.query.filter_by.get(id)

    if not register_lesse_to_delete:
        return {"message": f'ID number {id} does not exists.'}, HTTPStatus.NOT_FOUND
    
    delete_in_db(register_lesse_to_delete)
    
    return "", HTTPStatus.NO_CONTENT

def update_record_lesse_by_id(id: int, data: dict):
    user_to_update = RecordLesseModel.query.get(id)

    for key, value in data.items():
        setattr(user_to_update, key, value)

    add_in_db(user_to_update)

    return user_to_update, HTTPStatus.OK
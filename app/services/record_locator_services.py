from sqlalchemy.exc import IntegrityError
from app.exc.not_found_error import NotFound
from http import HTTPStatus
from app.models.record_locator_model import RecordLocatorModel
from app.models.user_locator_model import UserLocatorModel
from app.services.helpers import check_incorrect_keys, check_missing_keys, add_in_db, delete_in_db
from http import HTTPStatus


def to_asses_locator(data:dict):
    
        required_keys = ["user_locator_id", "user_lessee_id", "date"]
        
        check_missing_keys(data, required_keys)
        check_incorrect_keys(data, required_keys)

        assess_locator = RecordLocatorModel(**data)
        add_in_db(assess_locator)
        resp = assess_locator

        return resp


def get_avaliation_locator(user_id:int):
    # name_locator = UserLocatorModel.query.get(user_id)
    user_locator = RecordLocatorModel.query.get(user_id)
    
    if not user_locator:
        raise NotFound

    return user_locator

def update_record_locator(data:dict, record_id:int):
    record_locator_updt = RecordLocatorModel.query.get(record_id)

    for key, value in data.items():
        setattr(record_locator_updt, key, value)
    
    add_in_db(record_locator_updt)

    return record_locator_updt, HTTPStatus.OK

def delete_record_locator_by_id(id: int):
    register_locator_to_delete = RecordLocatorModel.query.filter_by.get(id)

    if not register_locator_to_delete:
        return {"message": f'ID number {id} does not exists.'}, HTTPStatus.NOT_FOUND
    
    delete_in_db(register_locator_to_delete)
    
    return "", HTTPStatus.NO_CONTENT

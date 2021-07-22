from sqlalchemy.sql.expression import true
from app.exc.not_permission import NotPermission
from app.exc.not_found_error import NotFound
from app.models.date_ocupied_model import DateOcupiedModel
from app.services.helpers import add_in_db ,format_url_date_ocupied, check_incorrect_keys, check_missing_keys, delete_in_db

def get_date_ocupied_by_car_id(car_id):
    date_ocupied = DateOcupiedModel.query.filter_by(car_id=car_id).all()

    return date_ocupied
    

def get_dates_ocupied_by_paginate(data):
    page_default, per_page_default = (1, 15)
    page = data.get("page") or page_default
    per_page = data.get("per_page") or per_page_default
    car_id = data.get("car_id") or 0
    unavaliable_date_id = data.get("unavaliable_date_id") or 0
    
    date_ocupied = DateOcupiedModel.query.filter(
        (DateOcupiedModel.car_id==int(car_id) or true), 
        (DateOcupiedModel.unavaliable_date_id==int(unavaliable_date_id) or True)).paginate(
            int(page), int(per_page),error_out=False)
    
    next_url, prev_url = format_url_date_ocupied(date_ocupied, page, per_page) 
    return date_ocupied, next_url, prev_url
    
def post_date_ocupied_by_data(data):
    
    required_keys = ("car_id", "unavaliable_date_id")
    check_incorrect_keys(data, required_keys)
    check_missing_keys(data, required_keys)
        
    date_ocupied = DateOcupiedModel(**data)
    add_in_db(date_ocupied)

    return date_ocupied


def delete_date_ocupied_by_id(id, token):
    date_to_delete = DateOcupiedModel.query.get(id)
    
    if not date_to_delete:
        raise NotFound
    
    delete_in_db(date_to_delete)
    
    return True
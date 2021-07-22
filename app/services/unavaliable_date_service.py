from app.exc.not_found_error import NotFound
from re import U
from app.models.unavaliable_date_model import UnavaliableDateModel
from app.services.helpers import add_in_db , check_incorrect_keys, check_missing_keys, delete_in_db, format_url_unavaliable_date
from ipdb import set_trace

def get_unavaliable_date_by_id(id):
    
    date_ocupied = UnavaliableDateModel.query.filter_by(id=id).first()
    
    if not date_ocupied:
        raise NotFound

    return date_ocupied
    

def get_unavaliable_date_by_paginate(data):
    
    page_default, per_page_default = (1, 15)
    
    page = data.get("page") or page_default
    per_page = data.get("per_page") or per_page_default
    date = data.get("date") or "1988-01-17"

    unavaliable_date = UnavaliableDateModel.query.filter(UnavaliableDateModel.date >= date).paginate(int(page), int(per_page),error_out=False)
    if not unavaliable_date:
        raise NotFound
    
    next_url, prev_url = format_url_unavaliable_date(unavaliable_date, page, per_page) 
    return unavaliable_date, next_url, prev_url
    
def post_unavaliable_date_by_data(data):
    required_keys = ["date"]
    
    check_incorrect_keys(data, required_keys)
    check_missing_keys(data, required_keys)

    unavaliable_date = UnavaliableDateModel(**data)
    add_in_db(unavaliable_date)

    return unavaliable_date


def delete_unavaliable_date_by_id(id):
    unavaliable_date = UnavaliableDateModel.query.get(id)
    
    if not unavaliable_date:
        raise NotFound 
    delete_in_db(unavaliable_date)
    return True
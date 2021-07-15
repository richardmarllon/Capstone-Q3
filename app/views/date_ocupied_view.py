from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required
from app.services.date_ocupied_services import delete_date_ocupied_by_id, post_date_ocupied_by_data ,get_date_ocupied_by_car_id, get_dates_ocupied_by_paginate

from app.exc.incorrect_keys_error import IncorrectKeysError
from app.exc.missing_keys_error import MissingKeys
from sqlalchemy.exc import IntegrityError
from http import HTTPStatus

from datetime import datetime

bp = Blueprint("date_ocupied", __name__, url_prefix="/date-ocupied")

@bp.get("/<int:car_id>")
@jwt_required()
def get_date_ocupied(car_id: int):
    date_ocupied = get_date_ocupied_by_car_id(car_id)
    
    if not date_ocupied:
        return {"msg": "not found"}, HTTPStatus.NOT_FOUND
    date_now = datetime.now()
    data_now_formated = date_now.strftime("%d/%m/%Y")

    return jsonify(date_ocupied), HTTPStatus.OK
    
@bp.get("/")
@jwt_required()
def get_dates_ocupied():
    
    data = request.args
        
    date_ocupied, next_url, prev_url = get_dates_ocupied_by_paginate(data)
    date_now = datetime.now()
    date_now_formated = date_now.strftime("%d/%m/%Y")

    return {"info": {"count": date_ocupied.total, "pages": date_ocupied.pages, "next_page": next_url, "prev_page": prev_url, }, "result": date_ocupied.items}, HTTPStatus.OK

@bp.post("/register")
@jwt_required()
def post_date_ocupied_register():
    try:
        
        data = request.get_json()
        date_ocupied = post_date_ocupied_by_data(data)
        
        return jsonify(date_ocupied), HTTPStatus.CREATED
    
    except IncorrectKeysError as e:
        return e.message, HTTPStatus.BAD_REQUEST
    except MissingKeys as e:
        return e.message, HTTPStatus.BAD_REQUEST
    except IntegrityError as e:
        error = {"message": str(e.__dict__['orig']) }
        return error, HTTPStatus.BAD_REQUEST
    
@bp.delete("/<int:id>")
@jwt_required()
def delete_date_ocupied(id: int):
    
    deleted = delete_date_ocupied_by_id(id)
    
    if not deleted:
        return {"message": f'ID number {id} does not exists.'}, HTTPStatus.NOT_FOUND
    return "", HTTPStatus.OK
    return {"message": "You need to be admin to delete the source."}, HTTPStatus.FORBIDDEN
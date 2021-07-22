from flask_jwt_extended.utils import get_jwt_identity
from app.exc.not_permission import NotPermission
from app.exc.not_found_error import NotFound
from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required
from app.services.date_ocupied_services import delete_date_ocupied_by_id, post_date_ocupied_by_data ,get_date_ocupied_by_car_id, get_dates_ocupied_by_paginate

from app.exc.incorrect_keys_error import IncorrectKeysError
from app.exc.missing_keys_error import MissingKeys
from sqlalchemy.exc import IntegrityError
from http import HTTPStatus

from datetime import datetime

bp = Blueprint("date_ocupied", __name__, url_prefix="/date-ocupied")

    
@bp.get("/")
@jwt_required()
def get_dates_ocupied():
    
    data = request.args
    date_ocupied, next_url, prev_url = get_dates_ocupied_by_paginate(data)

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
    
    try:
        token = get_jwt_identity()
        deleted = delete_date_ocupied_by_id(id, token)
        
        return "", HTTPStatus.OK
    
    except NotFound as e:
        return e.message
    except NotPermission as e:
        return e.message 
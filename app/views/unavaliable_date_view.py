from sqlalchemy import exc
from app.exc.not_found_error import NotFound
from flask import Blueprint, request, jsonify
from flask_jwt_extended import get_jwt_identity, jwt_required

from app.exc.incorrect_keys_error import IncorrectKeysError
from app.exc.missing_keys_error import MissingKeys
from sqlalchemy.exc import IntegrityError
from http import HTTPStatus

from app.services.unavaliable_date_service import delete_unavaliable_date_by_id, get_unavaliable_date_by_id, get_unavaliable_date_by_paginate, post_unavaliable_date_by_data

bp = Blueprint("unavaliable_date", __name__, url_prefix="/unavaliable-date")

@bp.post("/register")
@jwt_required()
def post_unavaliable_date_register():
    try:
        data = request.get_json()
        
        unavaliable_date = post_unavaliable_date_by_data(data)

        return jsonify(unavaliable_date), HTTPStatus.CREATED 
    
    except IncorrectKeysError as e:
        return e.message, HTTPStatus.BAD_REQUEST
    except MissingKeys as e:
        return e.message, HTTPStatus.BAD_REQUEST
    except IntegrityError as e:
        error = {"message": str(e.__dict__['orig']) }
        return error, HTTPStatus.BAD_REQUEST
    
@bp.get("/<int:id>")
@jwt_required()
def get_unavaliable_date(id: int):
    
    try:
        unavaliable_date = get_unavaliable_date_by_id(id)
        return jsonify(unavaliable_date), HTTPStatus.OK
    except NotFound as e:
        return e.message , HTTPStatus.NOT_FOUND

@bp.delete("/<int:id>")
@jwt_required()
def delete_unavaliable_date(id: int):
    
    try:
        deleted = delete_unavaliable_date_by_id(id)
    
        return "", HTTPStatus.OK
    except NotFound as e:
        return e.message , HTTPStatus.NOT_FOUND
        

@bp.get("/")
@jwt_required()
def get_dates_ocupied():
    
    data = request.args
        
    date_ocupied, next_url, prev_url = get_unavaliable_date_by_paginate(data)

    return {"info": {"count": date_ocupied.total, "pages": date_ocupied.pages, "next_page": next_url, "prev_page": prev_url, }, "result": date_ocupied.items}, HTTPStatus.OK

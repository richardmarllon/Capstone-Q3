from flask import Flask, Blueprint, request, jsonify
from http import HTTPStatus
from app.services.car_services import get_car_by_id, post_car_by_data, update_car_by_id, delete_car_by_id, get_car_by_filters
from app.exc.incorrect_keys_error import IncorrectKeysError
from app.exc.missing_keys_error import MissingKeys
from app.exc.not_permission import NotPermission 
from app.exc.not_found_error import NotFound

from flask_jwt_extended import jwt_required, get_jwt_identity
from sqlalchemy.exc import IntegrityError
 

bp = Blueprint("car", __name__, url_prefix="/car")

@bp.post("/register")
@jwt_required()
def post_car_register() -> tuple:
    current_user: dict = get_jwt_identity()
    data: dict = request.get_json()
    data["user_id"] = current_user["user_id"]
    
    try:
        response = post_car_by_data(data, current_user)
        return jsonify(response), HTTPStatus.CREATED
        
    except NotPermission as e:
            return e.message, HTTPStatus.UNAUTHORIZED

    except IncorrectKeysError as e:
        return e.message, HTTPStatus.BAD_REQUEST
        
    except MissingKeys as e:
        return e.message, HTTPStatus.BAD_REQUEST

    except IntegrityError as err:
        response = {"message": str(err.__dict__['orig']) }
        return response, HTTPStatus.BAD_REQUEST

@bp.patch("/update/<int:car_id>")
@jwt_required()
def patch_car_update(car_id: int) -> tuple:
    current_user: dict = get_jwt_identity()
    data: dict = request.get_json()
    data["user_id"] = current_user["user_id"]

    try:
        response = update_car_by_id(car_id, data, current_user) 
        return jsonify(response), HTTPStatus.OK
       
    except NotPermission as e:
            return e.message, HTTPStatus.UNAUTHORIZED
    

@bp.delete("/delete/<int:car_id>")
@jwt_required()
def del_car_delete(car_id: int) -> tuple:
    current_user = get_jwt_identity()
        
    try:
        response: str = delete_car_by_id(car_id, current_user)        
        return response, HTTPStatus.NO_CONTENT

    except NotFound as err:
        return err.message, HTTPStatus.NOT_FOUND
    
    except NotPermission as e:
            return e.message, HTTPStatus.UNAUTHORIZED

        
@bp.get("/")
@jwt_required()
def get_cars():

    try:
        data = request.args
        response = get_car_by_filters(**data)

        return response, HTTPStatus.OK

    except NotFound as err:
        return err.message, HTTPStatus.UNAUTHORIZED


@bp.get("/<int:car_id>")
@jwt_required()
def get_car(car_id: int) -> tuple:
    
    try:
        response = get_car_by_id(car_id)
        return response, HTTPStatus.OK

    except NotFound as err:
        return err.message, HTTPStatus.NOT_FOUND
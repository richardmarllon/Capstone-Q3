from flask import Flask, Blueprint, request, jsonify
from http import HTTPStatus

from sqlalchemy.sql.coercions import expect
from app.services.car_services import post_car_by_data, update_car_by_id, delete_car_by_id
from app.exc.incorrect_keys_error import IncorrectKeysError
from app.exc.missing_keys_error import MissingKeys
from app.exc.not_permission import Not_Permission 
from flask_jwt_extended import jwt_required, get_jwt_identity

 

bp = Blueprint("car", __name__, url_prefix="/car")

@bp.post("/register")
# @jwt_required()
def post_car_register():
    try:
        data = request.get_json()
        response = post_car_by_data(data)
        return response, HTTPStatus.CREATED

    except IncorrectKeysError as e:
        return e.message, HTTPStatus.BAD_REQUEST
        
    except MissingKeys as e:
        return e.message, HTTPStatus.BAD_REQUEST

@bp.patch("/update/<int:car_id>")
@jwt_required()
def patch_car_update(car_id: int):
    current_user = get_jwt_identity()
    data = request.get_json()
    try:
        if data["user_id"] == current_user["user_id"]:
                
            response = update_car_by_id(car_id, data) 
            return response, HTTPStatus.OK
        raise Not_Permission 
       
    except Not_Permission as e:
            return e.message, HTTPStatus.UNAUTHORIZED
  

@bp.delete("/delete/<int:car_id>")
@jwt_required()
def del_car_delete(car_id: int):
    current_user = get_jwt_identity()
        
    try:
        response = delete_car_by_id(car_id, current_user)        
        if not response:
            return "", HTTPStatus.NO_CONTENT

        raise Not_Permission

    
    except Not_Permission as e:
            return e.message, HTTPStatus.UNAUTHORIZED

    except:
        return {"message": f'ID_car number {car_id} does not exists.'}, HTTPStatus.BAD_REQUEST
@bp.get("/cars")
def get_cars(): 
    return "carro", HTTPStatus.OK


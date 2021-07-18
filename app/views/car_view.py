from flask import Flask, Blueprint, request, jsonify
from http import HTTPStatus
from app.services.car_services import get_car_by_id, post_car_by_data, update_car_by_id, delete_car_by_id, get_car_by_filters
from app.exc.incorrect_keys_error import IncorrectKeysError
from app.exc.missing_keys_error import MissingKeys
from app.exc.not_permission import NotPermission 
from flask_jwt_extended import jwt_required, get_jwt_identity
from sqlalchemy.exc import IntegrityError
 

bp = Blueprint("car", __name__, url_prefix="/car")

@bp.post("/register")
@jwt_required()
def post_car_register():
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
def patch_car_update(car_id: int):
    current_user = get_jwt_identity()
    data = request.get_json()
    try:
        if data["user_id"] == current_user["user_id"]:
                
            response = update_car_by_id(car_id, data) 
            return jsonify(response), HTTPStatus.OK
        raise NotPermission 
       
    except NotPermission as e:
            return e.message, HTTPStatus.UNAUTHORIZED
  

@bp.delete("/delete/<int:car_id>")
@jwt_required()
def del_car_delete(car_id: int):
    current_user = get_jwt_identity()
        
    try:
        response = delete_car_by_id(car_id, current_user)        
        if not response:
            return "", HTTPStatus.NO_CONTENT

        raise NotPermission

    
    except NotPermission as e:
            return e.message, HTTPStatus.UNAUTHORIZED

    except:
        return {"message": f'ID car {car_id} does not exists.'}, HTTPStatus.BAD_REQUEST
        
@bp.get("/cars/")
@jwt_required()
def get_cars():

    try:

        data = request.args
        cars, next_url, prev_url, total, pages = get_car_by_filters(**data)

        return {"info": {"count": total, "pages": pages, "next_page": next_url, "prev_page": prev_url}, "result": cars.items }, HTTPStatus.OK

    except NotPermission as e:
        e.message, HTTPStatus.UNAUTHORIZED


@bp.get("/<int:car_id>")
@jwt_required()
def get_car(car_id: int):
    
    car = get_car_by_id(car_id)
    if car:
        return {"car": car, "date_ocupied": car.date_ocupied, "avaliations": car.record_lessee }
    return {"msg": "not found"}, HTTPStatus.NOT_FOUND
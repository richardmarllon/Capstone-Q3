from flask import Flask, Blueprint, request, jsonify
from http import HTTPStatus
from app.services.car_services import post_car_by_data, update_car_by_id
from app.exc.incorrect_keys_error import IncorrectKeysError
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
        return e.message

@bp.patch("/update/<int:car_id>")
# @jwt_required()
def patch_car_update(car_id: int):
    # current_user = get_jwt_identity()
        data = request.get_json()
    # if data["user_id"] == current_user["user_id"]:
        response = update_car_by_id(car_id, data) 
       
        return response, HTTPStatus.OK
        # return {"message": "You need to own the source to modify."}, HTTPStatus.FORBIDDEN

@bp.delete("/delete/<int:car_id>")
def del_car_delete():
    return "", HTTPStatus.NO_CONTENT

@bp.get("/cars")
def get_cars(): 
    return "carro", HTTPStatus.OK


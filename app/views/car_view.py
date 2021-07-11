from flask import Flask, Blueprint, request, jsonify
from http import HTTPStatus

bp = Blueprint("car", __name__, url_prefix="/car")

@bp.post("/register")
def post_car_register():
    return "registrado", HTTPStatus.CREATED

@bp.patch("/update/<int:car_id>")
def patch_car_update():
    return "atalizado", HTTPStatus.OK

@bp.delete("/delete/<int:car_id>")
def del_car_delete():
    return "", HTTPStatus.NO_CONTENT

@bp.get("/cars")
def get_cars(): 
    return "carro", HTTPStatus.OK


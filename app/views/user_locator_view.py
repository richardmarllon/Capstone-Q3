from app.exc.not_permission import NotPermission
from app.exc.not_found_error import NotFound
from flask import Flask, Blueprint, request, jsonify
from flask_jwt_extended import jwt_required ,create_access_token, set_access_cookies, unset_jwt_cookies, get_jwt_identity

from ipdb import set_trace

from sqlalchemy.exc import IntegrityError
from app.exc.incorrect_keys_error import IncorrectKeysError
from app.services.user_locator_services import delete_user_locator_by_id, update_user_locator_by_id, get_users_locators_by_filters, post_user_locator_by_data, get_user_locator_by_cpf, get_user_locator_by_id

from http import HTTPStatus

bp = Blueprint("locator", __name__, url_prefix="/locator")

@bp.post("/register")
def post_user_locator_register():
    try:
        data = request.get_json()
        user = post_user_locator_by_data(data)
        return jsonify(user), HTTPStatus.CREATED
    except IncorrectKeysError as e:
        return e.message, HTTPStatus.BAD_REQUEST
    except IntegrityError as e:
        error = {"message": str(e.__dict__['orig']) }
        return error, HTTPStatus.BAD_REQUEST

@bp.post("/login")
def post_user_locator_login():
    try:
        data = request.get_json()
        user = get_user_locator_by_cpf(data)

        access_token = create_access_token(identity={"user_id": user.id, "user_name": user.name})
        response = jsonify({"msg": "login successful"})
        set_access_cookies(response, access_token)

        return {"access token": access_token}, HTTPStatus.OK

    except NotFound as e:
        return e.message, HTTPStatus.NOT_FOUND
        
@bp.get("/user/<int:user_id>")
@jwt_required()
def get_user_locator(user_id: int):
    
    try:
        token = get_jwt_identity()
        user = get_user_locator_by_id(user_id, token)

        return jsonify({"user": user,"user_cars": user.car}), HTTPStatus.OK
    
    except NotFound as e:
        return e.message, HTTPStatus.NOT_FOUND
    except NotPermission as e:
        return e.message, HTTPStatus.UNAUTHORIZED
    
    
@bp.patch("/update/<int:user_id>")
@jwt_required()
def patch_user_locator_update(user_id: int):
    
    try:
        current_user = get_jwt_identity()
        data = request.get_json()
        
        user_updated = update_user_locator_by_id(user_id, data, current_user)
    
        return jsonify(user_updated), HTTPStatus.OK
    
    except NotPermission as e:
        return e.message, HTTPStatus.UNAUTHORIZED
    except NotFound as e:
        return e.message, HTTPStatus.NOT_FOUND

@bp.delete("/delete/<int:user_id>")
@jwt_required()
def del_user_lessee_delete(user_id: int):
    
    try:
    
        current_user = get_jwt_identity()

        deleted = delete_user_locator_by_id(user_id, current_user)

        return "", HTTPStatus.OK

    
    except NotFound as e:
        return e.message, HTTPStatus.NOT_FOUND
    except NotPermission as e:
        return e.message, HTTPStatus.UNAUTHORIZED
       
#^(..)/(..)/(....)$
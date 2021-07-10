from flask import Flask, Blueprint, request, jsonify
from flask_jwt_extended import create_access_token, set_access_cookies, unset_jwt_cookies, get_current_user

from sqlalchemy.exc import IntegrityError
from app.exc.incorrect_keys_error import IncorrectKeysError
from app.services.user_locator_services import post_user_locator_by_data, get_user_locator_by_cpf

from http import HTTPStatus

bp = Blueprint("locator", __name__, url_prefix="/locator")

@bp.post("/register")
def post_user_locator_register():
    try:
        data = request.get_json()
        user = post_user_locator_by_data(data)
        return user
    except IncorrectKeysError as e:
        return e.message
    except IntegrityError as e:
        error = str(e.__dict__['orig'])
        return error, HTTPStatus.BAD_REQUEST

@bp.post("/login")
def post_user_locator_login():
    data = request.get_json()
    user = get_user_locator_by_cpf(data)

    access_token = create_access_token(identity="example_user")
    response = jsonify({"msg": "login successful"})
    set_access_cookies(response, access_token)
    access_token = create_access_token(identity="diego")

    return user.serialized()


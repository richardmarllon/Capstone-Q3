from flask import Flask, Blueprint, request, jsonify
from http import HTTPStatus
from app.exc.incorrect_keys_error import IncorrectKeysError
from sqlalchemy.exc import IntegrityError
from app.services.user_locator_services import post_user_locator_by_data
import re
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

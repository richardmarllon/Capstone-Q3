from sqlalchemy.exc import IntegrityError
from app.exc.incorrect_keys_error import IncorrectKeysError
from flask import Blueprint, request, jsonify
from http import HTTPStatus
from app.exc.incorrect_keys_error import IncorrectKeysError
from app.models.user_lesse_model import UserLesseModel
from app.services.user_lesse_services import post_user_lesse_by_data
import ipdb

bp = Blueprint("lesse",__name__, url_prefix="/lesse")

@bp.post("/register")
def post_user_lesse_register():
    try:
        data = request.get_json()
        response = post_user_lesse_by_data(data)
        # ipdb.set_trace()
        return response

    except IncorrectKeysError as err:
        return err.message

    except IntegrityError as err:
        response = {"message": str(err.__dict__['orig']) }
        return response, HTTPStatus.BAD_REQUEST



@bp.post("/login")
def post_user_lesse_login():
    ...

@bp.patch("/update/<int:user_id>")
def patch_user_lesse_update(user_id: int):
    ...

@bp.delete("/update/<int:user_id>")
def del_user_lesse_delete(user_id: int):
    ...

@bp.get("/user")
def get_user_lesse():
    ...


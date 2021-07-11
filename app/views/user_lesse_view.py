from sqlalchemy.exc import IntegrityError
from app.exc.incorrect_keys_error import IncorrectKeysError
from flask import Blueprint, request, jsonify
from http import HTTPStatus
from app.exc.incorrect_keys_error import IncorrectKeysError
from app.models.user_lesse_model import UserLesseModel
from app.services.user_lesse_services import post_user_lesse_by_data, search_user_lesse_by_cpf, delete_user_lesse_by_id, update_user_less_by_id
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
    data = request.get_json()
    try:
        return update_user_less_by_id(user_id, data)
    except KeyError as err:
        return {"message": "You can't change the password, yet!"}, HTTPStatus.UNAUTHORIZED

@bp.delete("/update/<int:user_id>")
def del_user_lesse_delete(user_id: int):
    return delete_user_lesse_by_id(user_id)
    


@bp.get("/user")
def get_user_lesse():
    cpf_to_search = request.get_json()
    try:
        return search_user_lesse_by_cpf(cpf_to_search)
        
    except IncorrectKeysError as err:
        return err.message

    except KeyError as err:
        return {"message": "User not found"}, HTTPStatus.NOT_FOUND

    


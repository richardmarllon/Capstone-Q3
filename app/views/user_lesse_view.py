from ipdb.__main__ import set_trace
from app.exc.missing_keys_error import MissingKeys
from sqlalchemy.exc import IntegrityError
from app.exc.incorrect_keys_error import IncorrectKeysError
from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from http import HTTPStatus
from app.exc.incorrect_keys_error import IncorrectKeysError
from app.models.user_lesse_model import UserLesseModel
from app.services.user_lesse_services import post_user_lesse_by_data, search_user_lesse_by_id, delete_user_lesse_by_id, update_user_less_by_id, login_user_lesse

bp = Blueprint("lesse",__name__, url_prefix="/lesse")

@bp.post("/register")
def post_user_lesse_register():
    try:
        data = request.get_json()
        response = post_user_lesse_by_data(data)
        return response, HTTPStatus.CREATED

    except IncorrectKeysError as err:
        return err.message, HTTPStatus.BAD_REQUEST
    except MissingKeys as err:
        return err.message, HTTPStatus.BAD_REQUEST

    except IntegrityError as err:
        response = {"message": str(err.__dict__['orig']) }
        return response, HTTPStatus.BAD_REQUEST



@bp.post("/login")
def post_user_lesse_login():
    data = request.get_json()
    try:
        return login_user_lesse(data), HTTPStatus.OK
    except IncorrectKeysError as err:
        return err.message, HTTPStatus.BAD_REQUEST
    except MissingKeys as err:
        return err.message, HTTPStatus.BAD_REQUEST
    except PermissionError:
        return {'message': "Bad credentials"}, HTTPStatus.UNAUTHORIZED
    except KeyError:
        return {"message": "User not found"}, HTTPStatus.NOT_FOUND


@bp.patch("/update/<int:user_id>")
@jwt_required()
def patch_user_lesse_update(user_id: int):
    current_user = get_jwt_identity()
    data = request.get_json()
    if user_id == current_user['user_id']:
            return update_user_less_by_id(user_id, data), HTTPStatus.OK
    return {"message": "You need to own the source to modify."}, HTTPStatus.FORBIDDEN


@bp.delete("/update/<int:user_id>")
@jwt_required()
def del_user_lesse_delete(user_id: int):
    current_user = get_jwt_identity()

    if user_id == current_user['user_id']:
        return delete_user_lesse_by_id(user_id), HTTPStatus.NO_CONTENT

    return {"message": "Sorry, something went wrong."}, HTTPStatus.BAD_REQUEST
    


@bp.get("/user/<int:user_id>")
def get_user_lesse(user_id):
    try:
        user = search_user_lesse_by_id(user_id)
        return {"user": user, "avaliations_received": user.record_locator, "avaliations_give": user.record_lesse}, HTTPStatus.OK
        
    except IncorrectKeysError as err:
        return err.message, HTTPStatus.BAD_REQUEST

    except KeyError as err:
        return {"message": "User not found"}, HTTPStatus.NOT_FOUND
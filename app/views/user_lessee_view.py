from ipdb.__main__ import set_trace
from app.exc.missing_keys_error import MissingKeys
from sqlalchemy.exc import IntegrityError
from app.exc.incorrect_keys_error import IncorrectKeysError
from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from http import HTTPStatus
from app.exc.incorrect_keys_error import IncorrectKeysError
from app.models.user_lessee_model import UserLesseeModel
from app.services.user_lessee_services import post_user_lessee_by_data, search_user_lessee_by_id, delete_user_lessee_by_id, update_user_lessee_by_id, login_user_lessee

bp = Blueprint("lesse",__name__, url_prefix="/lessee")

@bp.post("/register")
def post_user_lessee_register():
    try:
        data = request.get_json()
        response = post_user_lessee_by_data(data)
        return jsonify(response), HTTPStatus.CREATED

    except IncorrectKeysError as err:
        return err.message, HTTPStatus.BAD_REQUEST
    except MissingKeys as err:
        return err.message, HTTPStatus.BAD_REQUEST
    except IntegrityError as err:
        response = {"message": str(err.__dict__['orig']) }
        return response, HTTPStatus.BAD_REQUEST



@bp.post("/login")
def post_user_lessee_login():
    data = request.get_json()
    try:
        user, token = login_user_lessee(data)
        return {"user": user,"access token": token}, HTTPStatus.OK
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
def patch_user_lessee_update(user_id: int):
    current_user = get_jwt_identity()
    data = request.get_json()
    if user_id == current_user['user_id']:
        user = update_user_lessee_by_id(user_id, data)
        return jsonify(user), HTTPStatus.OK
    return {"message": "You need to own the source to modify."}, HTTPStatus.FORBIDDEN


@bp.delete("/update/<int:user_id>")
@jwt_required()
def del_user_lessee_delete(user_id: int):
    current_user = get_jwt_identity()

    if user_id == current_user['user_id']:
        return delete_user_lessee_by_id(user_id), HTTPStatus.NO_CONTENT

    return {"message": "not found"}, HTTPStatus.NOT_FOUND
    


@bp.get("/user/<int:user_id>")
def get_user_lessee(user_id):
    try:
        user = search_user_lessee_by_id(user_id)
        return {"user": user, "avaliations_received": user.record_locator, "avaliations_give": user.record_lessee}, HTTPStatus.OK
        
    except IncorrectKeysError as err:
        return err.message, HTTPStatus.BAD_REQUEST

    except KeyError as err:
        return {"message": "User not found"}, HTTPStatus.NOT_FOUND
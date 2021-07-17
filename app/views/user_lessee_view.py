from app.exc.not_permission import NotPermission
from app.exc.not_found_error import NotFound
from app.exc.bad_credentials_error import BadCredentials
from app.exc.missing_keys_error import MissingKeys
from sqlalchemy.exc import IntegrityError
from app.exc.incorrect_keys_error import IncorrectKeysError
from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from http import HTTPStatus
from app.exc.incorrect_keys_error import IncorrectKeysError
from app.services.user_lessee_services import post_user_lessee_by_data, search_user_lessee_by_id, delete_user_lessee_by_id, update_user_lessee_by_id, login_user_lessee

bp = Blueprint("lesse",__name__, url_prefix="/lessee")

@bp.post("/register")
def post_user_lessee_register():
    try:
        data: dict = request.get_json()
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
    data: dict = request.get_json()
    try:
        response = login_user_lessee(data)
        return response, HTTPStatus.OK
    except IncorrectKeysError as err:
        return err.message, HTTPStatus.BAD_REQUEST
    except MissingKeys as err:
        return err.message, HTTPStatus.BAD_REQUEST
    except BadCredentials as err:
        return err.message, HTTPStatus.UNAUTHORIZED
    except NotFound as err:
        return err.message, HTTPStatus.NOT_FOUND


@bp.patch("/update/<int:user_id>")
@jwt_required()
def patch_user_lessee_update(user_id: int):
    current_user: dict = get_jwt_identity()
    data: dict = request.get_json()
    try: 
        user = update_user_lessee_by_id(user_id, data, current_user)
        return jsonify(user), HTTPStatus.OK
    except NotPermission as err:
        return err.message, HTTPStatus.UNAUTHORIZED


@bp.delete("/update/<int:user_id>")
@jwt_required()
def del_user_lessee_delete(user_id: int):
    current_user: dict = get_jwt_identity()

    try:
        response: str = delete_user_lessee_by_id(user_id, current_user)
        return response, HTTPStatus.NO_CONTENT
    except NotFound as err:
        return err.message, HTTPStatus.NOT_FOUND
    except NotPermission as err:
        return err.message, HTTPStatus.UNAUTHORIZED

    


@bp.get("/user/<int:user_id>")
def get_user_lessee(user_id):
    try:
        user = search_user_lessee_by_id(user_id)
        return user, HTTPStatus.OK
        
    except IncorrectKeysError as err:
        return err.message, HTTPStatus.BAD_REQUEST

    except NotFound as err:
        return err.message, HTTPStatus.NOT_FOUND
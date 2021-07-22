from app.exc.not_permission import NotPermission
from app.exc.not_found_error import NotFound
from app.exc.missing_keys_error import MissingKeys
from sqlalchemy.exc import IntegrityError
from app.exc.incorrect_keys_error import IncorrectKeysError
from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from http import HTTPStatus
from app.exc.incorrect_keys_error import IncorrectKeysError
from app.services.record_lessee_services import post_record_lessee_by_data, search_record_lessee_by_id, delete_record_lessee_by_id, update_record_lessee_by_id

bp = Blueprint("rec-lessee",__name__, url_prefix="/record/lesse")

@bp.post("/register")
def post_record_lessee_register():
    data = request.get_json()

    try:
        response = post_record_lessee_by_data(data)
        return jsonify(response)
    except IncorrectKeysError as err:
        return err.message
    except MissingKeys as err:
        return err.message
    except IntegrityError as err:
        response = {"message": str(err.__dict__['orig']) }
        return response, HTTPStatus.BAD_REQUEST


@bp.patch("/update/<int:user_id>")
@jwt_required()
def patch_record_lessee_update(user_id: int):
    data = request.get_json()

    try:
        response = update_record_lessee_by_id(user_id, data)
        return jsonify(response)
    except NotPermission as err:
        return err.message, HTTPStatus.UNAUTHORIZED


@bp.delete("/delete/<int:user_id>")
@jwt_required()
def del_record_lessee_delete(user_id: int):

    try:
        return delete_record_lessee_by_id(user_id)
    except NotPermission as err:
        return err.message, HTTPStatus.UNAUTHORIZED
    


@bp.get("/<int:id>")
def get_record_lessee(id: int):
    try:
        response = search_record_lessee_by_id(id)
        return jsonify(response)
    
    except IncorrectKeysError as err:
        return err.message
    except NotFound as err:
        return err.message, HTTPStatus.NOT_FOUND
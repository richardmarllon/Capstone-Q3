from app.exc.missing_keys_error import MissingKeys
from sqlalchemy.exc import IntegrityError
from app.exc.incorrect_keys_error import IncorrectKeysError
from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from http import HTTPStatus
from app.exc.incorrect_keys_error import IncorrectKeysError
from app.services.record_lesse_services import post_record_lesse_by_data, search_record_lesse_by_id, delete_record_lesse_by_id, update_record_lesse_by_id

bp = Blueprint("rec-lesse",__name__, url_prefix="/rlesse")

@bp.post("/register_lesse")
def post_record_lesse_register():
    try:
        data = request.get_json()
        response = post_record_lesse_by_data(data)
        return jsonify(response)

    except IncorrectKeysError as err:
        return err.message
    except MissingKeys as err:
        return err.message

    except IntegrityError as err:
        response = {"message": str(err.__dict__['orig']) }
        return response, HTTPStatus.BAD_REQUEST


@bp.patch("/register_lesse/<int:user_id>")
@jwt_required()
def patch_record_lesse_update(user_id: int):
    current_user = get_jwt_identity()
    data = request.get_json()

    if user_id == current_user['user_id']:
            return jsonify(update_record_lesse_by_id(user_id, data))
    return {"message": "You need to own the source to modify."}, HTTPStatus.FORBIDDEN


@bp.delete("/register_lesse/<int:user_id>")
@jwt_required()
def del_record_lesse_delete(id: int):
    current_user = get_jwt_identity()
    if id == current_user['user_id']:
        return delete_record_lesse_by_id(id)
    return {"message": "You need to own the source to modify."}, HTTPStatus.FORBIDDEN
    


@bp.get("/register_lesse/<int:id>")
def get_record_lesse(id):
    try:
        return jsonify(search_record_lesse_by_id(id))
        
    except IncorrectKeysError as err:
        return err.message

    except KeyError as err:
        return {"message": "User not found"}, HTTPStatus.NOT_FOUND
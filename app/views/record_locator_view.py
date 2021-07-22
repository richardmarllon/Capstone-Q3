from flask_jwt_extended.utils import get_jwt_identity
from flask_jwt_extended.view_decorators import jwt_required
from app.exc.not_found_error import NotFound
from app.exc.incorrect_keys_error import IncorrectKeysError
from app.exc.missing_keys_error import MissingKeys
from app.exc.not_permission import NotPermission
from flask import Blueprint, jsonify, request, json
from http import HTTPStatus
from app.services.record_locator_services import to_asses_locator, get_avaliation_locator, update_record_locator, delete_record_locator_by_id

bp = Blueprint("record-locator", __name__, url_prefix="/record")

@bp.post("/locator/register")
@jwt_required()
def send_note_record_locator():
    try:
        data = request.get_json()

        resp = to_asses_locator(data)

        return jsonify(resp)

    except MissingKeys as error:
        return error.message, HTTPStatus.BAD_REQUEST
        
    except IncorrectKeysError as error:
        return error.message, HTTPStatus.BAD_REQUEST

    except PermissionError as error:
        return error, HTTPStatus.UNAUTHORIZED

@bp.get("/locator/<int:user_id>")
@jwt_required()
def avaliations_locator(user_id: int):
    
    user_locator = get_avaliation_locator(user_id)

    try:
        return jsonify(user_locator), HTTPStatus.OK

    except NotFound as err:
        return err.message, HTTPStatus.NOT_FOUND



@bp.patch("/locator/update/<int:avaliation_id>")
@jwt_required()
def update_avaliation(avaliation_id):
    try:
        data = request.get_json()
        record_locator = update_record_locator(data, avaliation_id)
        return jsonify(record_locator), HTTPStatus.OK
    except NotFound as err:
        return err.message, HTTPStatus.NOT_FOUND


@bp.delete("/locator/delete/<int:user_id>")
@jwt_required()
def del_record_lessee_delete(user_id: int):

    try:
        return delete_record_locator_by_id(user_id)
    except NotPermission as err:
        return err.message, HTTPStatus.UNAUTHORIZED
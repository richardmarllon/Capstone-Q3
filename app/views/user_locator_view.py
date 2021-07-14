from flask import Flask, Blueprint, request, jsonify
from flask_jwt_extended import jwt_required ,create_access_token, set_access_cookies, unset_jwt_cookies, get_jwt_identity

from ipdb import set_trace

from sqlalchemy.exc import IntegrityError
from app.exc.incorrect_keys_error import IncorrectKeysError
from app.services.user_locator_services import delete_user_locator_by_id, update_user_locator_by_id, get_users_locators_by_filters, post_user_locator_by_data, get_user_locator_by_cpf, get_user_locator_by_id

from http import HTTPStatus

bp = Blueprint("locator", __name__, url_prefix="/locator")

@bp.post("/register")
def post_user_locator_register():
    try:
        data = request.get_json()
        user = post_user_locator_by_data(data)
        return user.serialized(), HTTPStatus.CREATED
    except IncorrectKeysError as e:
        return e.message, HTTPStatus.BAD_REQUEST
    except IntegrityError as e:
        error = str(e.__dict__['orig'])
        return error, HTTPStatus.BAD_REQUEST

@bp.post("/login")
def post_user_locator_login():
    data = request.get_json()
    user = get_user_locator_by_cpf(data)

    if user:
        access_token = create_access_token(identity={"user_id": user.id, "user_name": user.name})
        response = jsonify({"msg": "login successful"})
        set_access_cookies(response, access_token)

        return {"access token": access_token}, HTTPStatus.OK
    return {"msg": "not found"}, HTTPStatus.NOT_FOUND

@bp.get("/users/<int:user_id>")
@jwt_required()
def get_user_locator(user_id: int):
    user = get_user_locator_by_id(user_id)
    token = get_jwt_identity()
    
    if not user:
        return {"msg": "not found"}, HTTPStatus.NOT_FOUND
    
    if token.get("user_id") != user.id:
        return {"msg": "unauthorized"}, HTTPStatus.UNAUTHORIZED
    return user.serialized(), HTTPStatus.OK
    
    
@bp.get("/users/")
@jwt_required()
def get_users_locators():
    
    data = request.args
    users, next_url, prev_url, total, pages = get_users_locators_by_filters(**data)

    return {"info": {"count": total, "pages": pages, "next_page": next_url, "prev_page": prev_url, }, "result": users.items}, HTTPStatus.OK

@bp.patch("/update/<int:user_id>")
@jwt_required()
def patch_user_locator_update(user_id: int):
    current_user = get_jwt_identity()
    data = request.get_json()
    if user_id == current_user['user_id']:
        user_updated = update_user_locator_by_id(user_id, data)
        return user_updated.serialized(), HTTPStatus.OK
    return {"message": "You need to own the source to modify."}, HTTPStatus.FORBIDDEN

@bp.delete("/delete/<int:user_id>")
@jwt_required()
def del_user_lesse_delete(user_id: int):
    current_user = get_jwt_identity()
    if user_id == current_user['user_id']:
        deleted = delete_user_locator_by_id(user_id)
        if not deleted:
            return {"message": f'ID number {id} does not exists.'}, HTTPStatus.NOT_FOUND
        return "", HTTPStatus.OK
    return {"message": "You need to own the source to modify."}, HTTPStatus.FORBIDDEN
       
#^(..)/(..)/(....)$
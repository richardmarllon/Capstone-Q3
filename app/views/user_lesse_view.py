from flask import Blueprint, request
from http import HTTPStatus

bp = Blueprint("lesse",__name__, url_prefix="/lesse")

@bp.post("/register")
def post_user_lesse_register():
    ...

@bp.post("/login")
def post_user_lesse_login():
    ...

@bp.patch("/update/<int:user_id>")
def patch_user_lesse_update(user_id: int):
    ...

@bp.delete("/update/<int:user_id>")
def del_user_lesse_delete(user_id: int):
    ...



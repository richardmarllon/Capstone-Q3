from flask import Blueprint

bp = Blueprint("unavaliable_date", __name__, url_prefix="/unavaliable_date")

@bp.get("/")
def get_unavaliable_date():
    pass
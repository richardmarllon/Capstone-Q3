from flask import Blueprint

bp = Blueprint("date_ocupied", __name__, url_prefix="/date-ocupied")

@bp.get("/")
def get_date_ocupied():
    pass
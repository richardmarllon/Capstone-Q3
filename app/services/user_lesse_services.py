from app.models.user_lesse_model import UserLesseModel
from app.services.helpers import add_in_db, check_incorrect_keys, format_cpf, criptography_string
from http import HTTPStatus
import ipdb

def post_user_lesse_by_data(data):
    required_keys = ["name", "last_name", "email", "city", "state", "cnh", "cpf", "password"]
    check_incorrect_keys(data, required_keys)


    cpf_to_encrypt = format_cpf(data)
    cpf_encrypted = criptography_string(cpf_to_encrypt) 
    data.pop("cpf")
    data["cpf_encrypt"] = cpf_encrypted

    lesse_user = UserLesseModel(**data)
    # ipdb.set_trace()
    add_in_db(lesse_user)


    return lesse_user.serialized(), HTTPStatus.CREATED


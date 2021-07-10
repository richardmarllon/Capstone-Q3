from app.models.user_locator_model import UserLocatorModel
from app.services.helpers import add_in_db, check_incorrect_keys, format_cpf, criptography_string
from http import HTTPStatus

from flask import current_app





def post_user_locator_by_data(data):
    required_keys = ["email", "password", "cpf", "name", "last_name", "address", "cep"]
    check_incorrect_keys(data, required_keys)

    cpf = format_cpf(data)
    cpf_to_insert = criptography_string(cpf)

    data.pop("cpf")
    data["cpf_encrypt"] = cpf_to_insert

    user = UserLocatorModel(**data)
    add_in_db(user)

    return user.serialized(), HTTPStatus.CREATED

def get_user_locator_by_cpf(data):
    cpf = format_cpf(data)
    cpf_to_search = criptography_string(cpf)

    user = UserLocatorModel.query.filter_by(cpf_encrypt=cpf_to_search).first()

    return user

from app.models.user_locator_model import UserLocatorModel
from app.services.helpers import add_in_db, check_incorrect_keys, format_cpf
from http import HTTPStatus

def post_user_locator_by_data(data):
    required_keys = ["email", "password", "cpf", "name", "last_name", "address", "cep"]
    check_incorrect_keys(data, required_keys)
    data["cpf"] = format_cpf(data)
    user = UserLocatorModel(**data)
    print(user)
    add_in_db(user)
    return user.serialized(), HTTPStatus.CREATED




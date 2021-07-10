from re import search
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

def search_user_lesse_by_cpf(data):
    required_keys = ["cpf"]
    check_incorrect_keys(data, required_keys)

    cpf_to_encrypt = format_cpf(data)
    cpf_encrypted = criptography_string(cpf_to_encrypt)

    search_result = UserLesseModel.query.filter_by(cpf_encrypt=cpf_encrypted).first()
    
    if not search_result:
        raise KeyError

    search_result = search_result.__dict__
    response = {k:v for k,v in search_result.items() if k in {'name', 'id', 'email', 'city', 'state', 'cnh'}}

    return response, HTTPStatus.OK




    




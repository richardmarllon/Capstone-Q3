from app.models.user_lesse_model import UserLesseModel
from app.services.helpers import add_in_db, check_incorrect_keys, format_cpf, criptography_string, delete_in_db, commit_current_session
from http import HTTPStatus
from flask_jwt_extended import create_access_token
import ipdb

def post_user_lesse_by_data(data) -> tuple:
    required_keys = ["name", "last_name", "email", "city", "state", "cnh", "cpf", "password"]
    check_incorrect_keys(data, required_keys)


    cpf_to_encrypt = format_cpf(data)
    cpf_encrypted = criptography_string(cpf_to_encrypt) 
    data.pop("cpf")
    data["cpf_encrypt"] = cpf_encrypted

    lesse_user = UserLesseModel(**data)
    add_in_db(lesse_user)
    response = lesse_user.serialized()


    return response, HTTPStatus.CREATED

def search_user_lesse_by_cpf(data) -> tuple:
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


def delete_user_lesse_by_id(id: int):
    user_to_delete = UserLesseModel.query.filter_by(id=id).first()

    if not user_to_delete:
        return {"message": f'ID number {id} does not exists.'}, HTTPStatus.NOT_FOUND
    
    delete_in_db(user_to_delete)
    
    return "", HTTPStatus.NO_CONTENT

def update_user_less_by_id(id: int, data: dict):
    user_to_update = UserLesseModel.query.filter_by(id=id).first()

    if data.get('password'):
        raise KeyError


    if data.get('cpf'):
        cpf_to_encrypt = format_cpf(data)
        cpf_encrypted = criptography_string(cpf_to_encrypt)
        data.pop("cpf")
        data["cpf_encrypt"] = cpf_encrypted
    

    user_to_update.name = data.get('name') or user_to_update.name
    user_to_update.email = data.get('email') or user_to_update.email
    user_to_update.last_name = data.get('last_name') or user_to_update.last_name
    user_to_update.city = data.get('city') or user_to_update.city
    user_to_update.state = data.get('state') or user_to_update.state
    user_to_update.cnh = data.get('cnh') or user_to_update.cnh

  
    commit_current_session()
    response = user_to_update.serialized()
    
    return response, HTTPStatus.OK

def login_user_lesse(data: dict):

    cpf_to_encrypt = format_cpf(data)
    cpf_encrypted = criptography_string(cpf_to_encrypt)
    user: UserLesseModel = UserLesseModel.query.filter_by(cpf_encrypt=cpf_encrypted).first()

    if not user:
        raise KeyError

    if user.check_password(data.get('password')):
        token = create_access_token(identity=user.name)
        response = user.serialized()
        response['access_token'] = token
        return response, HTTPStatus.OK
    else:
        return {'message': "Bad credentials"}, HTTPStatus.UNAUTHORIZED
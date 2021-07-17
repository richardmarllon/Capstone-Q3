from dataclasses import dataclass
from sqlalchemy.sql.elements import Null
from app.exc.not_found_error import NotFound
from app.exc.bad_credentials_error import BadCredentials
from app.models.user_lessee_model import UserLesseeModel
from app.services.helpers import add_in_db, check_incorrect_keys, check_missing_keys, check_user, format_cpf, criptography_string, delete_in_db, commit_current_session
from werkzeug.security import generate_password_hash
from flask_jwt_extended import create_access_token
import ipdb

def post_user_lessee_by_data(data: dict):
    required_keys: list = ["name", "last_name", "email", "city", "state", "cnh", "cpf", "password"]
    check_incorrect_keys(data, required_keys)
    check_missing_keys(data, required_keys)


    cpf_to_encrypt = format_cpf(data)
    cpf_encrypted = criptography_string(cpf_to_encrypt) 
    data.pop("cpf")
    data["cpf_encrypt"] = cpf_encrypted

    lesse_user: UserLesseeModel = UserLesseeModel(**data)
    add_in_db(lesse_user)


    return lesse_user

def search_user_lessee_by_id(id: int):

    user: dict = UserLesseeModel.query.filter_by(id=id).first()
    
    if not user:
        raise NotFound
    
    response: dict = {"user": user, "avaliations_received": user.record_locator, "avaliations_give": user.record_lessee}

    return response


def delete_user_lessee_by_id(id: int, current_user: dict):
    check_user(id, current_user)

    user_to_delete = UserLesseeModel.query.filter_by(id=id).first()

    delete_in_db(user_to_delete)
    
    return ""

def update_user_lessee_by_id(id: int, data: dict, current_user: dict):
    check_user(id, current_user)

    user_to_update: UserLesseeModel = UserLesseeModel.query.filter_by(id=id).first()

    if data.get('password'):
        new_password = generate_password_hash(data.get('password'))
        user_to_update.password_hash = new_password
        
    if data.get('cpf'):
        cpf_to_encrypt = format_cpf(data)
        cpf_encrypted = criptography_string(cpf_to_encrypt)
        data.pop("cpf")
        data["cpf_encrypt"] = cpf_encrypted
    
    
    for key, value in data.items():
        setattr(user_to_update, key, value)
    
    commit_current_session()
    response = user_to_update
    
    return response

def login_user_lessee(data: dict):
    required_keys = ["cpf", "password"]
    check_incorrect_keys(data, required_keys)
    check_missing_keys(data, required_keys)


    cpf_to_encrypt = format_cpf(data)
    cpf_encrypted = criptography_string(cpf_to_encrypt)
    user: UserLesseeModel = UserLesseeModel.query.filter_by(cpf_encrypt=cpf_encrypted).first()

    if not user:
        raise NotFound

    if user.check_password(data.get('password')):
        token: str = create_access_token(identity={"user_name": user.name, "user_id": user.id})
        response = {"user": user,"access token": token}
        return response
    else:
        raise BadCredentials
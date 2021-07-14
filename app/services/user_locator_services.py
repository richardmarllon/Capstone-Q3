from os import name
from app.models.user_locator_model import UserLocatorModel
from app.services.helpers import format_url_user_locator ,format_query_user_locator ,add_in_db, check_incorrect_keys, format_cpf, criptography_string, delete_in_db, decriptography_string
from http import HTTPStatus
from werkzeug.security import generate_password_hash

from flask import current_app

from ipdb import set_trace



def post_user_locator_by_data(data):
    required_keys = ["email", "password", "cpf", "name", "last_name", "address", "cep"]
    check_incorrect_keys(data, required_keys)

    cpf = format_cpf(data)
    cpf_to_insert = criptography_string(cpf)

    data.pop("cpf")
    data["cpf_encrypt"] = cpf_to_insert
    
    user = UserLocatorModel(**data)
    add_in_db(user)

    return user

def get_user_locator_by_cpf(data):
    cpf = format_cpf(data)
    cpf_to_search = criptography_string(cpf)

    
   
    user = UserLocatorModel.query.filter_by(cpf_encrypt=cpf_to_search).first()

    return user

def get_user_locator_by_id(data):
    
    user = UserLocatorModel.query.get(data)
    
    return user

def get_users_locators_by_filters(**data):
    
    name, last_name, cep, email, page, per_page = format_query_user_locator(data)
    return_users = []
     
    users = UserLocatorModel.query.filter(
        UserLocatorModel.name.like(name),
        UserLocatorModel.last_name.like(last_name),
        UserLocatorModel.cep.like(cep),
        UserLocatorModel.email.like(email)).paginate(int(page), int(per_page),error_out=False)
    print(users.has_prev)
    next_url, prev_url = format_url_user_locator(users.has_next, users.has_prev, users.next_num, users.prev_num, per_page, data)
    


    return (users, next_url, prev_url, users.total, users.pages)

def update_user_locator_by_id(id: int, data: dict):
    user_to_update = UserLocatorModel.query.get(id)

    if data.get('password'):
        new_password = generate_password_hash(data.get('password'))
        data.pop("password")
        data["password_hash"] = new_password
        
    if data.get('cpf'):
        cpf_to_encrypt = format_cpf(data)
        cpf_encrypted = criptography_string(cpf_to_encrypt)
        data.pop("cpf")
        data["cpf_encrypt"] = cpf_encrypted
        
    for key, value in data.items():
        setattr(user_to_update, key, value)
    
    add_in_db(user_to_update)
    
    return user_to_update

def delete_user_locator_by_id(id):
    user_to_delete = UserLocatorModel.query.get(id)
    
    if not user_to_delete:
        return False
    delete_in_db(user_to_delete)
    return True
    
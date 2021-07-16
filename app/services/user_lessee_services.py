from app.models.user_lessee_model import UserLesseeModel
from app.services.helpers import add_in_db, check_incorrect_keys, check_missing_keys, format_cpf, criptography_string, delete_in_db, commit_current_session
from werkzeug.security import generate_password_hash
from flask_jwt_extended import create_access_token

def post_user_lessee_by_data(data: dict):
    required_keys = ["name", "last_name", "email", "city", "state", "cnh", "cpf", "password"]
    check_incorrect_keys(data, required_keys)
    check_missing_keys(data, required_keys)


    cpf_to_encrypt = format_cpf(data)
    cpf_encrypted = criptography_string(cpf_to_encrypt) 
    data.pop("cpf")
    data["cpf_encrypt"] = cpf_encrypted

    lesse_user = UserLesseeModel(**data)
    add_in_db(lesse_user)
    response = lesse_user


    return response

def search_user_lessee_by_id(id: int):

    search_result = UserLesseeModel.query.filter_by(id=id).first()

    if not search_result:
        raise KeyError

    return search_result


def delete_user_lessee_by_id(id: int):
    user_to_delete = UserLesseeModel.query.filter_by(id=id).first()

    delete_in_db(user_to_delete)
    
    return ""

def update_user_lessee_by_id(id: int, data: dict):
    user_to_update = UserLesseeModel.query.filter_by(id=id).first()

    if data.get('password'):
        new_password = generate_password_hash(data.get('password'))
        user_to_update.password_hash = new_password
        
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
    response = user_to_update
    
    return response

def login_user_lessee(data):
    required_keys = ["cpf", "password"]
    check_incorrect_keys(data, required_keys)
    check_missing_keys(data, required_keys)


    cpf_to_encrypt = format_cpf(data)
    cpf_encrypted = criptography_string(cpf_to_encrypt)
    user: UserLesseeModel = UserLesseeModel.query.filter_by(cpf_encrypt=cpf_encrypted).first()

    if not user:
        raise KeyError

    if user.check_password(data.get('password')):
        token = create_access_token(identity={"user_name": user.name, "user_id": user.id})
        
        return user, token
    else:
        raise PermissionError
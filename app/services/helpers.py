import ipdb
from ipdb.__main__ import set_trace
from app.exc.missing_keys_error import MissingKeys
from flask import current_app
from app.exc.incorrect_keys_error import IncorrectKeysError
from werkzeug.security import generate_password_hash
import re
import pyDes

def add_in_db(data) -> None:
    session = get_current_session()
    session.add(data)
    session.commit()



def add_all_in_db(data) -> None:
    session = get_current_session()
    session.add_all(data)
    session.commit()


def delete_in_db(data) -> None:
    session = get_current_session()
    session.delete(data)
    session.commit()


def commit_current_session() -> None:
    session = current_app.db.session
    session.commit()


def get_current_session():
    return current_app.db.session()

def check_incorrect_keys(data, required_keys) -> None:
    wrong_keys = [keys for keys in data.keys() if keys not in required_keys]
    if wrong_keys:
        raise IncorrectKeysError(wrong_keys, required_keys)

def format_cpf(data):
    return "".join(re.split("[/.-]", data.get("cpf")))

def format_name(data):
    return

def criptography_string(data):
    key = current_app.config["CRIPTOGRAPHY_SECRET_KEY"]
    k = pyDes.des("DESCRYPT", pyDes.CBC, str(key), pad=None, padmode=pyDes.PAD_PKCS5)
    string_criptographed = str(k.encrypt(data))
    return string_criptographed

def decriptography_string(data):
    
    key = current_app.config["CRIPTOGRAPHY_SECRET_KEY"]
    k = pyDes.des("DESCRYPT", pyDes.CBC, str(key), pad=None, padmode=pyDes.PAD_PKCS5)
    string_criptographed = str(k.decrypt(data.split("'")[1].encode()))
    return string_criptographed


def format_car_plate(data) -> str:
    return "".join(re.findall('[0-9A-Za-z]', data.get("car_plate")))

def check_missing_keys(data: dict, required_keys: list):
    missing_keys = [key for key in required_keys if key not in data.keys()]
    if missing_keys:
        raise MissingKeys(missing_keys, required_keys)
    
def format_url_user_locator(has_next, has_prev, next_page_number, prev_page_number, per_page, data):

    name, email, cep, last_name = ("", "", "", "")
        
    next_url = None
    prev_url = None
      
    if data.get("name"):
        name = "&name={}".format(data.get("name"))
        
    if data.get("last_name"):
        last_name = "&last_name={}".format(data.get("last_name")) 
          
    if data.get("cep"):
        cep = "&cep={}".format(data.get("cep"))
        
    if data.get("email"):
        email = "&email={}".format(data.get("email"))
        
                   
    if has_next and next_page_number:
        next_url = f"https://capstone-q3.herokuapp.com/locator/users/?per_page={per_page}&page={next_page_number}" + name + last_name + cep + email
    if has_prev and prev_page_number:    
        prev_url = f"https://capstone-q3.herokuapp.com/locator/users/?per_page={per_page}&page={prev_page_number}" + name + last_name + cep + email
    
    return (next_url, prev_url)
    
def format_query_user_locator(data):
    default_page = 1
    default_per_page = 15
    default_value = ""
    
    name = "%{}%".format(data.get("name") or default_value)
    last_name = "%{}%".format(data.get("last_name") or default_value)
    cep = "%{}%".format(data.get("cep") or default_value)
    email = "%{}%".format(data.get("email") or default_value)
    page = data.get("page") or default_page
    per_page = data.get("per_page") or default_per_page
    
    return (name, last_name, cep, email, page, per_page)
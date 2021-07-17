from app.exc.not_permission import NotPermission
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
    
def format_url_date_ocupied(date_ocupied, page, per_page):
    next_url = None
    prev_url = None
    
    if date_ocupied.has_next and date_ocupied.next_num:
        next_url = f"https://capstone-q3.herokuapp.com/date-ocupied/?per_page={per_page}&page={page}"
    if date_ocupied.has_prev and date_ocupied.prev_num:    
        prev_url = f"https://capstone-q3.herokuapp.com/date-ocupied/?per_page={per_page}&page={page}"
    
    return next_url, prev_url
def format_url_unavaliable_date(date_ocupied, page, per_page):
    next_url = None
    prev_url = None
    
    if date_ocupied.has_next and date_ocupied.next_num:
        next_url = f"https://capstone-q3.herokuapp.com/date-ocupied/?per_page={per_page}&page={page}"
    if date_ocupied.has_prev and date_ocupied.prev_num:    
        prev_url = f"https://capstone-q3.herokuapp.com/date-ocupied/?per_page={per_page}&page={page}"
    
    return next_url, prev_url
        
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

def format_query_car(data: dict):
    default_page = 1
    default_per_page = 15
    default_value=""
    
    year = data.get("year") or 0
    thunk_volume = data.get("thunk_volume") or 0
    
    model ="%{}%".format(data.get("model") or default_value)
    withdrawal_place ="%{}%".format(data.get("withdrawal_place") or default_value)
    city ="%{}%".format(data.get("city") or default_value)
    state ="%{}%".format(data.get("state") or default_value)
    page = data.get("page") or default_page
    per_page = data.get("per_page") or default_per_page

    return ( year, model, thunk_volume, withdrawal_place, city, state, page, per_page)


def format_url_car(has_next, has_prev, next_page_number, prev_page_number, per_page, data):
    
    year, model, thunk_volume, withdrawal_place, city, state = ("","","","","","")

    next_url = None
    prev_url = None

    if data.get("year"):
        year = "&year={}".format(data.get("year"))

    if data.get("model"):
        model = "&model={}".format(data.get("model"))

    if data.get("thunk_volume"):
        thunk_volume = "&thunk_volume={}".format(data.get("thunk_volume"))

    if data.get("withdrawal_place"):
        withdrawal_place = "&withdrawal_place={}".format(data.get("withdrawal_place"))

    if data.get("city"):
        city = "&city={}".format(data.get("city"))

    if data.get("state"):
        state = "&state={}".format(data.get("state"))

    if has_next and next_page_number:
        next_url = f"http://127.0.0.1:5000/car/cars/?per_page={per_page}&page={next_page_number}" + year + model + thunk_volume + withdrawal_place + city + state
    
    if has_prev and prev_page_number:
        prev_url = f"http://127.0.0.1:5000/car/cars/?per_page={per_page}&page={prev_page_number}" + year + model + thunk_volume + withdrawal_place + city + state
    
    return (next_url, prev_url)

    
def check_user(user_id, current_user):
    if not user_id == current_user['user_id']:
        raise NotPermission
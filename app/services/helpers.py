import ipdb
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
    string_criptographed = "a"
    return string_criptographed

def check_missing_keys(data: dict, required_keys: list):
    missing_keys = [key for key in required_keys if key not in data.keys()]
    if missing_keys:
        raise MissingKeys(missing_keys, required_keys)

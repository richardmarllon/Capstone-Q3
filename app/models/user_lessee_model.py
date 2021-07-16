from app.configs.database import db
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy import Column, Integer, String, Text
from dataclasses import dataclass

@dataclass
class UserLesseeModel(db.Model):
    id: int
    name:str
    last_name: str
    city: str
    state: str
    email: str

    __tablename__ = "user_lessee"

    id = Column(Integer, primary_key=True)

    name = Column(String(55), nullable=False)
    last_name = Column(String(55), nullable=False)
    email = Column(String(255), nullable=False, unique=True)
    city = Column(String(55), nullable=False)
    state = Column(String(2), nullable=False)
    cnh = Column(Text, nullable=False, unique=True)

    cpf_encrypt = Column(String(255), nullable=False, unique=True)
    password_hash = Column(String(), nullable=False)

    @property
    def password(self):
        raise AttributeError("Cannot be accessed.")

    @password.setter
    def password(self, password_to_hash:str) -> str:
        self.password_hash = generate_password_hash(password_to_hash)
    
    def check_password(self, password_to_check:str) -> bool:
        return check_password_hash(self.password_hash, password_to_check)
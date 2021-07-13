from app.configs.database import db
from sqlalchemy import Column, Integer, String, Text, Unicode
from werkzeug.security import check_password_hash, generate_password_hash
from dataclasses import dataclass

@dataclass
class UserLocatorModel(db.Model):
    
    id: int
    name: str
    last_name: str
    email: str
    password_hash: str
    cpf_encrypt: str
    address: str
    cep: str
    
    __tablename__ = "user_locator"

    id = Column(Integer, primary_key=True)

    name = Column(String(55), nullable=False)
    last_name = Column(String(55), nullable=False)
    email = Column(String(255), nullable=False, unique=True)
    password_hash = Column(String(), nullable=False)
    cpf_encrypt = Column(Unicode(), nullable=False, unique=True)
    address = Column(Text, nullable=False)
    cep = Column(String(10), nullable=False)

    @property
    def password(self):
        raise AttributeError("Password cannot be accessed!")

    @password.setter
    def password(self, password_to_hash):
        self.password_hash = generate_password_hash(password_to_hash)

    def check_password(self, password_to_compare):
        return check_password_hash(self.password_hash, password_to_compare)

    def serialized(self):
        return {"name": self.name, "email": self.email, "cep": self.cep, "address": self.address}

    def __repr__(self):
        return {"name": self.name, "id": self.id}

    def __str__(self):
        return f"id: {self.id}, name:{self.name}"

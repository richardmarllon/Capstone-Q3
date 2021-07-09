from app.configs.database import db
from sqlalchemy import Column, Integer, String, Text
from werkzeug.security import check_password_hash, generate_password_hash

class UserLocatorModel(db.Model):
    __tablename__ = "user_locator"

    id = Column(Integer, primary_key=True)

    name = Column(String(55), nullable=False)
    last_name = Column(String(55), nullable=False)
    email = Column(String(255), nullable=False, unique=True)
    password_hash = Column(String(), nullable=False)
    cpf_hash = Column(String(), nullable=False, unique=True)
    address = Column(Text, nullable=False)
    cep = Column(String(10), nullable=False)

    @property
    def cpf(self):
        raise AttributeError("CPF cannot be accessed")

    @cpf.setter
    def cpf(self, cpf_to_hash):
        self.cpf_hash = generate_password_hash(cpf_to_hash)

    def verify_cpf(self, cpf_to_compare):
        return check_password_hash(self.cpf_hash, cpf_to_compare)

    def serialized(self):
        return {"name": self.name, "email": self.email, "cep": self.cep, "address": self.address}

    @property
    def password(self):
        raise AttributeError("Password cannot be accessed!")

    @password.setter
    def password(self, password_to_hash):
        self.password_hash = generate_password_hash(password_to_hash)

    def check_password(self, password_to_compare):
        return check_password_hash(self.password_hash, password_to_compare)

    def __repr__(self):
        return {"name": self.name, "id": self.id}

    def __str__(self):
        return f"id: {self.id}, name:{self.name}"

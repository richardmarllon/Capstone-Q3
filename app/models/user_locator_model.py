from app.configs.database import db
from sqlalchemy import Column, Integer, String, Text
from werkzeug.security import check_password_hash, generate_password_hash

class UserLocatorModel(db.model):
    __tablename__ = "user_locator"

    id = Column(Integer, primary_key=True)

    name = Column(String(55), nullable=True)
    email = Column(String(255), nullable=True, unique=True)
    password = Column(String(55), nullable=True)
    cpf = Column(String(11), nullable=False, unique=True)
    adress = Column(Text, nullable=True)
    cep = Column(String(10), nullable=True)

    @property
    def cpf(self):
        raise AttributeError("CPF cannot be acessed")

    @cpf.setter
    def cpf(self, cpf_to_hash):
        self.cpf = generate_password_hash(cpf_to_hash)

    def verify_cpf(self, cpf_to_compare):
        return check_password_hash(self.cpf, cpf_to_compare)

    def serialized(self):
        return {"name": self.name, "email": self.email, "cep": self.cep, "adress": self.adress}

    def __repr__(self):
        return {"model": self.model, "user_id": self.user_id, "id": self.id}

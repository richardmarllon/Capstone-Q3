from app.configs.database import db
from sqlalchemy.orm import relationship, backref
from sqlalchemy import Column, Integer, Text, Date, ForeignKey
from dataclasses import dataclass

@dataclass
class RecordLesseModel(db.Model):
    id: int
    lesse_id: int
    car_id: int
    avaliation: int
    comment: str
    date: str

    __tablename__ = "record_lesse"

    id = Column(Integer, primary_key=True)

    date = Column(Date)
    comment = Column(Text, nullable=False)
    avaliation = Column(Integer)
    car_id = Column(Integer, ForeignKey("car.id"), nullable=False)
    lesse_id = Column(Integer, ForeignKey("user_lesse.id"), nullable=False)

    car = relationship("CarModel", backref=backref("record_lesse"))
    lesse = relationship("UserLesseModel", backref=backref("record_lesse"))

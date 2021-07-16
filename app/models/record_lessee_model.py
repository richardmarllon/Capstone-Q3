from app.configs.database import db
from sqlalchemy.orm import relationship, backref
from sqlalchemy import Column, Integer, Text, Date, ForeignKey
from dataclasses import dataclass

@dataclass
class RecordLesseeModel(db.Model):
    id: int
    lessee_id: int
    car_id: int
    avaliation: int
    comment: str
    date: str

    __tablename__ = "record_lessee"

    id = Column(Integer, primary_key=True)

    date = Column(Date, nullable=False)
    comment = Column(Text, default=None)
    avaliation = Column(Integer, default=None)
    car_id = Column(Integer, ForeignKey("car.id"), nullable=False)
    lessee_id = Column(Integer, ForeignKey("user_lessee.id"), nullable=False)

    car = relationship("CarModel", backref=backref("record_lessee"))
    lessee = relationship("UserLesseeModel", backref=backref("record_lessee"))

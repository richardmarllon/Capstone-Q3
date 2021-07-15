from dataclasses import dataclass
from app.configs.database import db
from sqlalchemy.orm import relationship, backref
from sqlalchemy import Column, Integer, ForeignKey


@dataclass
class DateOcupiedModel(db.Model):
    __tablename__ = "date_ocupied"

    id: int
    car_id: int
    unavaliable_date: int
      
    id = Column(Integer, primary_key=True)

    car_id = Column(Integer, ForeignKey("car.id"), nullable=False)
    unavaliable_date_id = Column(Integer, ForeignKey("unavaliable_date.id"), nullable=False)

    car = relationship("CarModel", backref=backref("date_ocupied"))
    unavaliable_date = relationship("UnavaliableDateModel", backref=backref("date_ocupied"))
    
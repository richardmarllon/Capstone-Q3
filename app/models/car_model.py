from dataclasses import dataclass
from datetime import date
from app.configs.database import db
from sqlalchemy.orm import relationship, backref
from sqlalchemy import Column, Integer, Date, String, ForeignKey
from dataclasses import dataclass


@dataclass
class CarModel(db.Model):
    __tablename__ = "car"

    id: int
    year: str
    model: str
    thunk_volume: int
    insurer: str
    insurer_number: str
    review_date: date
    withdrawal_place: str 
    city: str
    state: str    
        
    id = Column(Integer, primary_key=True)

    year = Column(Integer, nullable=False)
    car_plate = Column(String(7), nullable=False,)
    model = Column(String(20), nullable=False)
    thunk_volume = Column(Integer, default=None)
    insurer = Column(String(55), nullable=False)
    insurer_number = Column(String(20), nullable=False)
    review_date = Column(Date, nullable=False)
    withdrawal_place = Column(String(255), nullable=False)
    city = Column(String(50), nullable=False)
    state = Column(String(2), nullable=False)

    user_id = Column(Integer, ForeignKey("user_locator.id"), nullable=False)

    user = relationship("UserLocatorModel", backref=backref("car"))
    def serialized(self):
        return {"model": self.model, "year": self.year, "car_plate": self.car_plate, "thunk_volume": self.thunk_volume,
                "insurer": self.insurer, "insurer_number": self.insurer_number, "review_date": self.review_date,
                "withdrawal_place": self.withdrawal_place, "city": self.city, "state": self.state, "user_id": self.user_id}

    def __repr__(self):
        return f'model: self.model, user_id: self.user_id, "id": self.id'

    def __str__(self):
        return f"id: {self.id}, model:{self.model}, user_id:{self.user_id}"

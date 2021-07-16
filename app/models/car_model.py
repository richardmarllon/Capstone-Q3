from dataclasses import dataclass
from app.configs.database import db
from sqlalchemy.orm import relationship, backref
from sqlalchemy import Column, Integer, Date, String, ForeignKey


@dataclass
class CarModel(db.Model):
    __tablename__ = "car"

    id: int
    year: int
    model: str
    thunk_volume: int
    insurer: str
    insurer_number: str
    review_date: str
    withdrawal_place: str 
    city: str
    state: str    
        
    id = Column(Integer, primary_key=True)

    year = Column(Integer, nullable=False)
    car_plate = Column(String(7), nullable=False, unique=True)
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
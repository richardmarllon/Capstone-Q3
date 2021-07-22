from dataclasses import dataclass
from app.configs.database import db
from sqlalchemy import Column, Integer, Date


@dataclass
class UnavaliableDateModel(db.Model):
    __tablename__ = "unavaliable_date"

    id: int
    date: str
    
    id = Column(Integer, primary_key=True)
    date = Column(Date, nullable=False)
    
from sqlalchemy.orm import relationship, backref
from dataclasses import dataclass
from sqlalchemy import Column, Integer, Date, ForeignKey
from sqlalchemy.sql.sqltypes import String
from app.configs.database import db


@dataclass
class RecordLocatorModel(db.Model):
    user_locator_id: int
    user_lessee_id: int
    comment: String
    date: Date
    avaliation: int

    __tablename__ = "record_locator"

    id=Column(Integer, primary_key=True)
    date=Column(Date)
    comment=Column(String(150), default=None)
    avaliation=Column(Integer, default=None)

    user_locator_id=Column(Integer, ForeignKey("user_locator.id"), nullable=False)
    user_lessee_id=Column(Integer,ForeignKey("user_lessee.id"), nullable=False)

    locator = relationship("UserLocatorModel", backref=backref("record_locator"))
    lessee = relationship("UserLesseeModel", backref=backref("record_locator"))


from database import Base
from sqlalchemy import Column, Integer, String, Float, DateTime


class MeasurementDB(Base):
    __tablename__ = "measurements"
    id = Column(Integer, primary_key=True, index=True)
    date = Column(DateTime)
    temp = Column(Float)
    hum = Column(Float)
    calAire = Column(String)
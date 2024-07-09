from pydantic import BaseModel
from datetime import datetime


class Measurement(BaseModel):
    date: datetime
    temp: float
    hum: float
    calAire: str
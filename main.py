from typing import List
from fastapi import FastAPI, Depends
from models import MeasurementDB, Base
from schemas import Measurement

from database import engine, get_db

from sqlalchemy.orm import Session


Base.metadata.create_all(bind=engine)

app = FastAPI()


@app.post("/create-measurement/", response_model=Measurement)
def create_measurement(measurement: Measurement, db: Session = Depends(get_db)):
    db_measurement = MeasurementDB(
        date=measurement.date,
        temp=measurement.temp,
        hum=measurement.hum,
        calAire=measurement.calAire,
    )
    db.add(db_measurement)
    db.commit()
    db.refresh(db_measurement)
    return db_measurement


@app.get("/get-all-measurements/", response_model=List[Measurement])
def read_measurements(db: Session = Depends(get_db)):
    return db.query(MeasurementDB).all()
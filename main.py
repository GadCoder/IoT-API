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


@app.get("/get-last-measurement/", response_model=Measurement)
def read_last_measurement(db: Session = Depends(get_db)):
    return db.query(MeasurementDB).order_by(MeasurementDB.id.desc()).first()


@app.get("/get-highest-temp-measurements/", response_model=List[Measurement])
def get_top_temp_measurements(db: Session = Depends(get_db)):
    return db.query(MeasurementDB).filter(MeasurementDB.calAire > 0.0, MeasurementDB.calAire < 4000.0).order_by(MeasurementDB.temp.desc()).limit(10).all()


@app.get("/get-lowest-temp-measurements/", response_model=List[Measurement])
def get_top_temp_measurements(db: Session = Depends(get_db)):
    return db.query(MeasurementDB).filter(MeasurementDB.calAire > 0.0, MeasurementDB.calAire < 4000.0).order_by(MeasurementDB.temp.asc()).limit(10).all()


@app.get("/get-highest-hum-measurements/", response_model=List[Measurement])
def get_top_hum_measurements( db: Session = Depends(get_db)):
    return db.query(MeasurementDB).filter(MeasurementDB.calAire > 0.0, MeasurementDB.calAire < 4000.0).order_by(MeasurementDB.hum.desc()).limit(10).all()


@app.get("/get-lowest-hum-measurements/", response_model=List[Measurement])
def get_top_hum_measurements( db: Session = Depends(get_db)):
    return db.query(MeasurementDB).filter(MeasurementDB.calAire > 0.0, MeasurementDB.calAire < 4000.0).order_by(MeasurementDB.hum.asc()).limit(10).all()


@app.get("/get-highest-calAire-measurements/", response_model=List[Measurement])   
def get_top_calAire_measurements(db: Session = Depends(get_db)):
    return db.query(MeasurementDB).filter(MeasurementDB.calAire > 0.0, MeasurementDB.calAire < 4000.0).order_by(MeasurementDB.calAire.desc()).limit(10).all()


@app.get("/get-lowest-calAire-measurements/", response_model=List[Measurement])   
def get_top_calAire_measurements(db: Session = Depends(get_db)):
    return db.query(MeasurementDB).filter(MeasurementDB.calAire > 0.0, MeasurementDB.calAire < 4000.0).order_by(MeasurementDB.calAire.asc()).limit(10).all()
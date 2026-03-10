from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles

from datetime import datetime
import pandas as pd
import os

import models
from database import engine, SessionLocal, get_db

app = FastAPI()

models.Base.metadata.create_all(bind=engine)

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

app.mount("/frontend", StaticFiles(directory=os.path.join(BASE_DIR, "frontend")), name="frontend")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# HOME
@app.get("/")
def home():
    return FileResponse("frontend/login.html")


# ---------------- VEHICLES ----------------

@app.post("/add_vehicle")
def add_vehicle(vehicle_name:str,vehicle_number:str,vehicle_type:str,unit_capacity:str,db:Session=Depends(get_db)):

    vehicle=models.Vehicle(
        vehicle_name=vehicle_name,
        vehicle_number=vehicle_number,
        vehicle_type=vehicle_type,
        unit_capacity=unit_capacity
    )

    db.add(vehicle)
    db.commit()

    return {"message":"Vehicle added"}


@app.get("/get_vehicles")
def get_vehicles(db:Session=Depends(get_db)):
    return db.query(models.Vehicle).all()


@app.put("/update_vehicle/{id}")
def update_vehicle(id:int,vehicle_name:str,vehicle_number:str,vehicle_type:str,unit_capacity:str,db:Session=Depends(get_db)):

    vehicle=db.query(models.Vehicle).filter(models.Vehicle.id==id).first()

    if not vehicle:
        return {"error":"Vehicle not found"}

    vehicle.vehicle_name=vehicle_name
    vehicle.vehicle_number=vehicle_number
    vehicle.vehicle_type=vehicle_type
    vehicle.unit_capacity=unit_capacity

    db.commit()

    return {"message":"Vehicle updated"}


# ---------------- DRIVERS ----------------

@app.post("/add_driver")
def add_driver(name:str,phone:str,license_number:str,db:Session=Depends(get_db)):

    driver=models.Driver(name=name,phone=phone,license_number=license_number)

    db.add(driver)
    db.commit()

    return {"message":"Driver added"}


@app.get("/get_drivers")
def get_drivers(db:Session=Depends(get_db)):
    return db.query(models.Driver).all()


@app.put("/update_driver/{id}")
def update_driver(id:int,name:str,phone:str,license_number:str,db:Session=Depends(get_db)):

    driver=db.query(models.Driver).filter(models.Driver.id==id).first()

    if not driver:
        return {"error":"Driver not found"}

    driver.name=name
    driver.phone=phone
    driver.license_number=license_number

    db.commit()

    return {"message":"Driver updated"}


# ---------------- TRIPS ----------------

@app.post("/add_trip")
def add_trip(
vehicle:str,
driver:str,
material_type:str,
units:float,
loading_location:str,
delivery_location:str,
customer:str,
loading_cost:float,
customer_payment:float,
start_date:str,
end_date:str,
start_time:str=None,
end_time:str=None,
db:Session=Depends(get_db)
):

    start_date_obj=datetime.strptime(start_date,"%Y-%m-%d").date()
    end_date_obj=datetime.strptime(end_date,"%Y-%m-%d").date()

    start_time_obj=None
    end_time_obj=None

    if start_time:
        start_time_obj=datetime.strptime(start_time,"%H:%M").time()

    if end_time:
        end_time_obj=datetime.strptime(end_time,"%H:%M").time()

    trip=models.Trip(
        vehicle=vehicle,
        driver=driver,
        material_type=material_type,
        units=units,
        loading_location=loading_location,
        delivery_location=delivery_location,
        customer=customer,
        loading_cost=loading_cost,
        customer_payment=customer_payment,
        start_date=start_date_obj,
        end_date=end_date_obj,
        start_time=start_time_obj,
        end_time=end_time_obj
    )

    db.add(trip)
    db.commit()

    return {"message":"Trip added"}


@app.get("/get_trips")
def get_trips(db:Session=Depends(get_db)):
    return db.query(models.Trip).all()


@app.put("/update_trip/{id}")
def update_trip(id:int,vehicle:str,driver:str,material_type:str,units:float,customer:str,customer_payment:float,db:Session=Depends(get_db)):

    trip=db.query(models.Trip).filter(models.Trip.id==id).first()

    if not trip:
        return {"error":"Trip not found"}

    trip.vehicle=vehicle
    trip.driver=driver
    trip.material_type=material_type
    trip.units=units
    trip.customer=customer
    trip.customer_payment=customer_payment

    db.commit()

    return {"message":"Trip updated"}


# ---------------- FUEL ----------------

@app.post("/add_fuel")
def add_fuel(vehicle:str,fuel_type:str,litres:float,rate:float,station:str,fuel_date:str=None,db:Session=Depends(get_db)):

    total_cost=litres*rate

    date_obj=None
    if fuel_date:
        date_obj=datetime.strptime(fuel_date,"%Y-%m-%d").date()

    fuel=models.Fuel(
        vehicle=vehicle,
        fuel_type=fuel_type,
        litres=litres,
        rate=rate,
        total_cost=total_cost,
        station=station,
        fuel_date=date_obj
    )

    db.add(fuel)
    db.commit()

    return {"message":"Fuel added"}


@app.get("/get_fuel")
def get_fuel(db:Session=Depends(get_db)):
    return db.query(models.Fuel).all()


@app.put("/update_fuel/{id}")
def update_fuel(id:int,vehicle:str,fuel_type:str,litres:float,rate:float,station:str,fuel_date:str=None,db:Session=Depends(get_db)):

    fuel=db.query(models.Fuel).filter(models.Fuel.id==id).first()

    if not fuel:
        return {"error":"Fuel not found"}

    fuel.vehicle=vehicle
    fuel.fuel_type=fuel_type
    fuel.litres=litres
    fuel.rate=rate
    fuel.total_cost=litres*rate
    fuel.station=station

    if fuel_date:
        fuel.fuel_date=datetime.strptime(fuel_date,"%Y-%m-%d").date()

    db.commit()

    return {"message":"Fuel updated"}


# ---------------- SALARY ----------------

@app.post("/add_salary")
def add_salary(driver_name:str,amount:float,notes:str="",salary_date:str=None,db:Session=Depends(get_db)):

    date_obj=None
    if salary_date:
        date_obj=datetime.strptime(salary_date,"%Y-%m-%d").date()

    salary=models.Salary(
        driver_name=driver_name,
        amount=amount,
        notes=notes,
        salary_date=date_obj
    )

    db.add(salary)
    db.commit()

    return {"message":"Salary added"}


@app.get("/get_salary")
def get_salary(db:Session=Depends(get_db)):
    return db.query(models.Salary).all()



@app.put("/update_salary/{id}")
def update_salary(id:int,driver_name:str,amount:float,notes:str="",salary_date:str=None,db:Session=Depends(get_db)):

    salary=db.query(models.Salary).filter(models.Salary.id==id).first()

    if not salary:
        return {"error":"Salary not found"}

    salary.driver_name=driver_name
    salary.amount=amount
    salary.notes=notes

    if salary_date:
        salary.salary_date=datetime.strptime(salary_date,"%Y-%m-%d").date()

    db.commit()

    return {"message":"Salary updated"}

@app.get("/get_attendance")
def get_attendance(db:Session=Depends(get_db)):

    attendance=db.query(models.Attendance).all()

    result=[]
    for a in attendance:
        result.append({
            "driver_name":a.driver_name,
            "date":str(a.date),
            "status":a.status
        })

    return result

@app.post("/add_attendance")
def add_attendance(driver_name:str,date:str,status:str,db:Session=Depends(get_db)):

    date_obj=datetime.strptime(date,"%Y-%m-%d").date()

    # check if attendance already exists
    record=db.query(models.Attendance).filter(
        models.Attendance.driver_name==driver_name,
        models.Attendance.date==date_obj
    ).first()

    if record:
        record.status=status
    else:
        attendance=models.Attendance(
            driver_name=driver_name,
            date=date_obj,
            status=status
        )
        db.add(attendance)

    db.commit()

    return {"message":"Attendance saved"}

@app.get("/export_full_report")
def export_full_report(db: Session = Depends(get_db)):

    trips = db.query(models.Trip).all()
    fuel = db.query(models.Fuel).all()
    salary = db.query(models.Salary).all()
    vehicles = db.query(models.Vehicle).all()
    drivers = db.query(models.Driver).all()
    attendance = db.query(models.Attendance).all()

    trip_data = []
    for t in trips:
        trip_data.append({
            "Vehicle": t.vehicle,
            "Driver": t.driver,
            "Material": t.material_type,
            "Units": t.units,
            "Customer": t.customer,
            "Payment": t.customer_payment,
            "Start Date": str(t.start_date),
            "End Date": str(t.end_date)
        })

    fuel_data = []
    for f in fuel:
        fuel_data.append({
            "Vehicle": f.vehicle,
            "Fuel Type": f.fuel_type,
            "Litres": f.litres,
            "Rate": f.rate,
            "Total Cost": f.total_cost,
            "Station": f.station,
            "Date": str(f.fuel_date)
        })

    salary_data = []
    for s in salary:
        salary_data.append({
            "Driver": s.driver_name,
            "Amount": s.amount,
            "Notes": s.notes,
            "Date": str(s.salary_date)
        })

    vehicle_data = []
    for v in vehicles:
        vehicle_data.append({
            "Name": v.vehicle_name,
            "Number": v.vehicle_number,
            "Type": v.vehicle_type,
            "Capacity": v.unit_capacity
        })

    driver_data = []
    for d in drivers:
        driver_data.append({
            "Name": d.name,
            "Phone": d.phone,
            "License": d.license_number
        })

    attendance_data = []
    for a in attendance:
        attendance_data.append({
            "Driver": a.driver_name,
            "Date": str(a.date),
            "Status": a.status
        })

    file_name = "transport_full_report.xlsx"

    with pd.ExcelWriter(file_name) as writer:
        pd.DataFrame(trip_data).to_excel(writer, sheet_name="Trips", index=False)
        pd.DataFrame(fuel_data).to_excel(writer, sheet_name="Fuel", index=False)
        pd.DataFrame(salary_data).to_excel(writer, sheet_name="Salary", index=False)
        pd.DataFrame(vehicle_data).to_excel(writer, sheet_name="Vehicles", index=False)
        pd.DataFrame(driver_data).to_excel(writer, sheet_name="Drivers", index=False)
        pd.DataFrame(attendance_data).to_excel(writer, sheet_name="Attendance", index=False)

    return FileResponse(file_name, filename="transport_full_report.xlsx")

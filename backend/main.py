from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles

from datetime import datetime, timedelta
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

# VEHICLES
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

# DRIVERS
@app.post("/add_driver")
def add_driver(name:str,phone:str,license_number:str,db:Session=Depends(get_db)):
    driver=models.Driver(name=name,phone=phone,license_number=license_number)
    db.add(driver)
    db.commit()
    return {"message":"Driver added"}

@app.get("/get_drivers")
def get_drivers(db:Session=Depends(get_db)):
    return db.query(models.Driver).all()

# CUSTOMERS
@app.post("/add_customer")
def add_customer(name:str,phone:str,location:str,db:Session=Depends(get_db)):
    customer=models.Customer(name=name,phone=phone,location=location)
    db.add(customer)
    db.commit()
    return {"message":"Customer added"}

@app.get("/get_customers")
def get_customers(db:Session=Depends(get_db)):
    return db.query(models.Customer).all()

# TRIPS
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

# FUEL
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

# SALARY
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

# MAINTENANCE
@app.post("/add_maintenance")
def add_maintenance(vehicle:str,maintenance_type:str,cost:float,workshop:str,maintenance_date:str=None,db:Session=Depends(get_db)):

    date_obj=None
    if maintenance_date:
        date_obj=datetime.strptime(maintenance_date,"%Y-%m-%d").date()

    item=models.Maintenance(
        vehicle=vehicle,
        maintenance_type=maintenance_type,
        cost=cost,
        workshop=workshop,
        maintenance_date=date_obj
    )

    db.add(item)
    db.commit()

    return {"message":"Maintenance added"}

@app.get("/get_maintenance")
def get_maintenance(db:Session=Depends(get_db)):
    return db.query(models.Maintenance).all()

# ATTENDANCE
@app.post("/add_attendance")
def add_attendance(driver_name:str,date:str,status:str,db:Session=Depends(get_db)):

    date_obj=datetime.strptime(date,"%Y-%m-%d").date()

    record=db.query(models.Attendance).filter(
        models.Attendance.driver_name==driver_name,
        models.Attendance.date==date_obj
    ).first()

    if record:
        record.status=status
    else:
        record=models.Attendance(driver_name=driver_name,date=date_obj,status=status)
        db.add(record)

    db.commit()

    return {"message":"Attendance saved"}

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

# EXPORTS
@app.get("/export_full_report")
def export_full_report(db: Session = Depends(get_db)):

    from fastapi.responses import FileResponse
    import pandas as pd

    # ---------------- TRIPS ----------------
    trips = db.query(models.Trip).all()

    trips_data = []
    for t in trips:
        trips_data.append({
            "Vehicle": t.vehicle,
            "Driver": t.driver,
            "Customer": t.customer,
            "Start Date": str(t.start_date),
            "End Date": str(t.end_date),
            "Payment": t.customer_payment
        })

    trips_df = pd.DataFrame(trips_data)


    # ---------------- FUEL ----------------
    fuels = db.query(models.Fuel).all()

    fuel_data = []
    for f in fuels:
        fuel_data.append({
            "Vehicle": f.vehicle,
            "Fuel Type": f.fuel_type,
            "Litres": f.litres,
            "Rate": f.rate,
            "Total": f.total_cost,
            "Station": f.station,
            "Date": str(f.fuel_date)
        })

    fuel_df = pd.DataFrame(fuel_data)


    # ---------------- MAINTENANCE ----------------
    maintenance = db.query(models.Maintenance).all()

    maint_data = []
    for m in maintenance:
        maint_data.append({
            "Vehicle": m.vehicle,
            "Type": m.maintenance_type,
            "Cost": m.cost,
            "Workshop": m.workshop,
            "Date": str(m.maintenance_date)
        })

    maint_df = pd.DataFrame(maint_data)


    # ---------------- SALARY ----------------
    salaries = db.query(models.Salary).all()

    salary_data = []
    for s in salaries:
        salary_data.append({
            "Driver": s.driver_name,
            "Amount": s.amount,
            "Notes": s.notes,
            "Date": str(s.salary_date)
        })

    salary_df = pd.DataFrame(salary_data)


    # ---------------- ATTENDANCE ----------------
    attendance = db.query(models.Attendance).all()

    att_data = []
    for a in attendance:
        att_data.append({
            "Driver": a.driver_name,
            "Date": str(a.date),
            "Status": a.status
        })

    att_df = pd.DataFrame(att_data)


    # ---------------- WRITE EXCEL ----------------
    file_path = "transport_full_report.xlsx"

    with pd.ExcelWriter(file_path) as writer:

        trips_df.to_excel(writer, sheet_name="Trips", index=False)
        fuel_df.to_excel(writer, sheet_name="Fuel", index=False)
        maint_df.to_excel(writer, sheet_name="Maintenance", index=False)
        salary_df.to_excel(writer, sheet_name="Salary", index=False)
        att_df.to_excel(writer, sheet_name="Attendance", index=False)


    return FileResponse(file_path, filename="transport_full_report.xlsx")
from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from database import engine, SessionLocal
import models
from fastapi.middleware.cors import CORSMiddleware
import pandas as pd
from fastapi.responses import FileResponse
from datetime import datetime, timedelta
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
import os

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


# DATABASE SESSION
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def home():
    return FileResponse("frontend/login.html")


# ADD VEHICLE
@app.post("/add_vehicle")
def add_vehicle(
    vehicle_name: str,
    vehicle_number: str,
    vehicle_type: str,
    unit_capacity: str,
    db: Session = Depends(get_db)
):
    new_vehicle = models.Vehicle(
        vehicle_name=vehicle_name,
        vehicle_number=vehicle_number,
        vehicle_type=vehicle_type,
        unit_capacity=unit_capacity
    )

    db.add(new_vehicle)
    db.commit()
    db.refresh(new_vehicle)

    return {"message": "Vehicle added successfully"}

@app.get("/get_vehicles")
def get_vehicles(db: Session = Depends(get_db)):
    vehicles = db.query(models.Vehicle).all()
    return vehicles

# ADD DRIVER
@app.post("/add_driver")
def add_driver(
    name: str,
    phone: str,
    license_number: str,
    db: Session = Depends(get_db)
):

    new_driver = models.Driver(
        name=name,
        phone=phone,
        license_number=license_number
    )

    db.add(new_driver)
    db.commit()
    db.refresh(new_driver)

    return {"message": "Driver added successfully"}

@app.get("/get_drivers")
def get_drivers(db: Session = Depends(get_db)):
    drivers = db.query(models.Driver).all()
    return drivers

# ADD CUSTOMER
@app.post("/add_customer")
def add_customer(
    name: str,
    phone: str,
    location: str,
    db: Session = Depends(get_db)
):

    new_customer = models.Customer(
        name=name,
        phone=phone,
        location=location
    )

    db.add(new_customer)
    db.commit()
    db.refresh(new_customer)

    return {"message": "Customer added successfully"}

@app.get("/get_customers")
def get_customers(db: Session = Depends(get_db)):
    customers = db.query(models.Customer).all()
    return customers
#ADD TRIP

from datetime import datetime

@app.post("/add_trip")
def add_trip(
    vehicle: str,
    driver: str,
    material_type: str,
    units: float,
    loading_location: str,
    delivery_location: str,
    customer: str,
    loading_cost: float,
    customer_payment: float,
    start_date: str,
    end_date: str,
    start_time: str = None,
    end_time: str = None,
    db: Session = Depends(get_db)
):

    start_date_obj = datetime.strptime(start_date, "%Y-%m-%d").date()
    end_date_obj = datetime.strptime(end_date, "%Y-%m-%d").date()

    start_time_obj = None
    end_time_obj = None

    if start_time:
        start_time_obj = datetime.strptime(start_time, "%H:%M").time()

    if end_time:
        end_time_obj = datetime.strptime(end_time, "%H:%M").time()

    new_trip = models.Trip(
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

    db.add(new_trip)
    db.commit()

    return {"message": "Trip added"}


@app.get("/get_trips")
def get_trips(db: Session = Depends(get_db)):
    trips = db.query(models.Trip).all()
    return trips

# ADD FUEL
from datetime import datetime

@app.post("/add_fuel")
def add_fuel(
    vehicle: str,
    fuel_type: str,
    litres: float,
    rate: float,
    station: str,
    fuel_date: str = None,
    db: Session = Depends(get_db)
):

    from datetime import datetime

    total_cost = litres * rate

    date_obj = None
    if fuel_date:
        date_obj = datetime.strptime(fuel_date,"%Y-%m-%d").date()

    new_fuel = models.Fuel(
        vehicle=vehicle,
        fuel_type=fuel_type,
        litres=litres,
        rate=rate,
        total_cost=total_cost,
        station=station,
        fuel_date=date_obj
    )

    db.add(new_fuel)
    db.commit()

    return {"message": "Fuel added"}
# ADD MAINTENANCE
from datetime import datetime

@app.post("/add_salary")
def add_salary(
    driver_name: str,
    amount: float,
    notes: str = "",
    salary_date: str = None,
    db: Session = Depends(get_db)
):

    from datetime import datetime

    date_obj = None
    if salary_date:
        date_obj = datetime.strptime(salary_date,"%Y-%m-%d").date()

    new_salary = models.Salary(
        driver_name=driver_name,
        amount=amount,
        notes=notes,
        salary_date=date_obj
    )

    db.add(new_salary)
    db.commit()

    return {"message":"Salary added"}

from datetime import datetime 
@app.delete("/delete_trip/{trip_id}")
def delete_trip(trip_id: int, db: Session = Depends(get_db)):

    trip = db.query(models.Trip).filter(models.Trip.id == trip_id).first()

    if not trip:
        return {"error": "Trip not found"}

    db.delete(trip)
    db.commit()

    return {"message": "Trip deleted"}

@app.delete("/delete_maintenance/{id}")
def delete_maintenance(id:int, db: Session = Depends(get_db)):

    item = db.query(models.Maintenance).filter(models.Maintenance.id == id).first()

    db.delete(item)
    db.commit()

    return {"message":"deleted"}

@app.delete("/delete_salary/{id}")
def delete_salary(id:int, db: Session = Depends(get_db)):

    item = db.query(models.Salary).filter(models.Salary.id == id).first()

    db.delete(item)
    db.commit()

    return {"message":"deleted"}
@app.delete("/delete_driver/{id}")
def delete_driver(id:int, db: Session = Depends(get_db)):

    item = db.query(models.Driver).filter(models.Driver.id == id).first()

    db.delete(item)
    db.commit()

    return {"message":"deleted"}
@app.delete("/delete_fuel/{id}")
def delete_fuel(id:int, db: Session = Depends(get_db)):

    item = db.query(models.Fuel).filter(models.Fuel.id == id).first()

    db.delete(item)
    db.commit()

    return {"message":"deleted"}

@app.delete("/delete_vehicle/{vehicle_id}")
def delete_vehicle(vehicle_id: int, db: Session = Depends(get_db)):

    vehicle = db.query(models.Vehicle).filter(models.Vehicle.id == vehicle_id).first()

    if not vehicle:
        return {"error": "Vehicle not found"}

    db.delete(vehicle)
    db.commit()

    return {"message": "Vehicle deleted"}

@app.get("/monthly_report")
def monthly_report(db: Session = Depends(get_db)):

    today = datetime.today().date()
    last_30_days = today - timedelta(days=30)

    trips = db.query(models.Trip).filter(
        models.Trip.start_date >= last_30_days
    ).all()

    report = {}

    for t in trips:

        date = str(t.start_date)

        if date not in report:
            report[date] = 0

        report[date] += t.customer_payment

    return report 

@app.get("/vehicle_report")
def vehicle_report(db: Session = Depends(get_db)):

    trips = db.query(models.Trip).all()

    report = {}

    for t in trips:

        if t.vehicle not in report:
            report[t.vehicle] = 0

        profit = t.customer_payment - t.loading_cost

        report[t.vehicle] += profit

    return report


@app.get("/export_excel")
def export_excel(db: Session = Depends(get_db)):

    trips = db.query(models.Trip).all()

    data = []

    for t in trips:
        data.append({
            "Vehicle": t.vehicle,
            "Driver": t.driver,
            "Material": t.material_type,
            "Units": t.units,
            "Customer": t.customer,
            "Payment": t.customer_payment,
            "Loading Cost": t.loading_cost,
            "Start Date": t.start_date,
            "End Date": t.end_date
        })

    df = pd.DataFrame(data)

    file_path = "transport_report.xlsx"

    df.to_excel(file_path, index=False)

    return FileResponse(file_path, filename="transport_report.xlsx")

@app.get("/get_fuel")
def get_fuel(db: Session = Depends(get_db)):
    fuel = db.query(models.Fuel).all()
    return fuel

@app.get("/get_maintenance")
def get_maintenance(db: Session = Depends(get_db)):
    maintenance = db.query(models.Maintenance).all()
    return maintenance

@app.get("/get_salary")
def get_salary(db: Session = Depends(get_db)):
    salary = db.query(models.Salary).all()
    return salary

@app.post("/add_maintenance")
def add_maintenance(
    vehicle: str,
    maintenance_type: str,
    cost: float,
    workshop: str,
    maintenance_date: str = None,
    db: Session = Depends(get_db)
):

    from datetime import datetime

    date_obj = None
    if maintenance_date:
        date_obj = datetime.strptime(maintenance_date,"%Y-%m-%d").date()

    new_maintenance = models.Maintenance(
        vehicle=vehicle,
        maintenance_type=maintenance_type,
        cost=cost,
        workshop=workshop,
        maintenance_date=date_obj
    )

    db.add(new_maintenance)
    db.commit()

    return {"message":"Maintenance added"}

@app.post("/add_attendance")
def add_attendance(driver_name:str,date:str,status:str,db:Session=Depends(get_db)):

    from datetime import datetime

    date_obj=datetime.strptime(date,"%Y-%m-%d").date()

    record=db.query(models.Attendance).filter(
        models.Attendance.driver_name==driver_name,
        models.Attendance.date==date_obj
    ).first()

    if record:
        record.status=status
    else:
        record=models.Attendance(
            driver_name=driver_name,
            date=date_obj,
            status=status
        )
        db.add(record)

    db.commit()

    return {"message":"Attendance saved"}

@app.get("/get_attendance")
def get_attendance(db: Session = Depends(get_db)):

    attendance = db.query(models.Attendance).all()

    return attendance

@app.get("/monthly_attendance")
def monthly_attendance(db: Session = Depends(get_db)):

    attendance = db.query(models.Attendance).all()

    report = {}

    for a in attendance:

        if a.driver_name not in report:
            report[a.driver_name] = 0

        if a.status == "Present":
            report[a.driver_name] += 1

    return report






@app.get("/export_fuel_excel")
def export_fuel_excel(db: Session = Depends(get_db)):

    fuels = db.query(models.Fuel).all()

    data = []
    for f in fuels:
        data.append({
            "Vehicle": f.vehicle,
            "Fuel Type": f.fuel_type,
            "Litres": f.litres,
            "Rate": f.rate,
            "Station": f.station,
            "Date": f.date
        })

    df = pd.DataFrame(data)

    file_path = "fuel_report.xlsx"
    df.to_excel(file_path, index=False)

    return FileResponse(file_path, filename="fuel_report.xlsx")

from fastapi.responses import FileResponse
import pandas as pd

@app.get("/export_fuel_excel")
def export_fuel_excel(db: Session = Depends(get_db)):

    fuels = db.query(models.Fuel).all()

    data = []
    for f in fuels:
        data.append({
            "Vehicle": f.vehicle,
            "Fuel Type": f.fuel_type,
            "Litres": f.litres,
            "Rate": f.rate,
            "Station": f.station,
            "Date": f.date
        })

    df = pd.DataFrame(data)

    file_path = "fuel_report.xlsx"
    df.to_excel(file_path, index=False)

    return FileResponse(file_path, filename="fuel_report.xlsx")

@app.get("/export_salary_excel")
def export_salary_excel(db: Session = Depends(get_db)):

    salaries = db.query(models.Salary).all()

    data = []
    for s in salaries:
        data.append({
            "Driver": s.driver_name,
            "Amount": s.amount,
            "Notes": s.notes,
            "Date": s.date
        })

    df = pd.DataFrame(data)

    file_path = "salary_report.xlsx"
    df.to_excel(file_path, index=False)

    return FileResponse(file_path, filename="salary_report.xlsx")
from sqlalchemy import Column, Integer, String, Date, Float
from .database import Base


# USERS (login)
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String)
    password = Column(String)


# VEHICLES
class Vehicle(Base):
    __tablename__ = "vehicles"

    id = Column(Integer, primary_key=True, index=True)
    vehicle_name = Column(String)
    vehicle_number = Column(String)
    vehicle_type = Column(String)   # lorry / jcb
    unit_capacity = Column(String)

    insurance_expiry = Column(Date)
    rc_expiry = Column(Date)


# DRIVERS
class Driver(Base):
    __tablename__ = "drivers"

    id = Column(Integer, primary_key=True, index=True)

    name = Column(String)
    phone = Column(String)

    license_number = Column(String)
    license_expiry = Column(Date)

    joining_date = Column(Date)


# CUSTOMERS
class Customer(Base):
    __tablename__ = "customers"

    id = Column(Integer, primary_key=True, index=True)

    name = Column(String)
    phone = Column(String)
    location = Column(String)


# TRIPS
from sqlalchemy import Column, Integer, String, Float, Date, Time

class Trip(Base):

    __tablename__="trips"

    id=Column(Integer,primary_key=True,index=True)

    vehicle=Column(String)
    driver=Column(String)

    material_type=Column(String)
    units=Column(Float)

    loading_location=Column(String)
    delivery_location=Column(String)

    customer=Column(String)

    loading_cost=Column(Float)
    customer_payment=Column(Float)

    start_date=Column(Date)
    end_date=Column(Date)

    start_time=Column(Time)
    end_time=Column(Time)
# FUEL
class Fuel(Base):
    __tablename__ = "fuel"

    id = Column(Integer, primary_key=True, index=True)

    vehicle = Column(String)
    fuel_type = Column(String)

    litres = Column(Float)
    rate = Column(Float)

    total_cost = Column(Float)

    station = Column(String)

    fuel_date = Column(Date)


# MAINTENANCE
class Maintenance(Base):
    __tablename__ = "maintenance"

    id = Column(Integer, primary_key=True, index=True)

    vehicle = Column(String)

    maintenance_type = Column(String)

    cost = Column(Float)

    workshop = Column(String)

    maintenance_date = Column(Date)


# SALARY
class Salary(Base):
    __tablename__ = "salary"

    id = Column(Integer, primary_key=True, index=True)

    driver_name = Column(String)

    amount = Column(Float)

    salary_date = Column(Date)

    notes = Column(String)

from sqlalchemy import Column, Integer, String, Date
from .database import Base


class Attendance(Base):

    __tablename__ = "attendance"

    id = Column(Integer, primary_key=True, index=True)

    driver_name = Column(String)

    date = Column(Date)

    status = Column(String)
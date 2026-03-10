# 🚍 Transport Management System

A full-stack **Transport Management System** developed using **HTML, CSS, JavaScript, FastAPI, and PostgreSQL**.
This system helps manage vehicles, drivers, trips, fuel records, maintenance, salary tracking, and driver attendance.

The project is deployed online and can be accessed from any device.

---

# 🌐 Live Project

Frontend: https://transport-system.vercel.app
Backend API: https://transport-system-1-i84e.onrender.com

API Documentation:
https://transport-system-1-i84e.onrender.com/docs

---

# 📌 Features

### 🔐 Authentication

* Login system using browser **localStorage**
* Session protection for all pages

### 🚗 Vehicle Management

* Add new vehicles
* View registered vehicles
* Store vehicle number, name and capacity

### 👨‍✈️ Driver Management

* Add driver details
* View driver list
* Used for attendance and trip assignments

### 📅 Driver Attendance

* Monthly calendar view
* Click a day to toggle attendance:

  * 🟢 Present
  * 🟡 Half Day
  * 🔴 Absent
* Save attendance to database

### 🗓️ Calendar Navigation

* Switch between months
* Attendance automatically loads for selected driver

### 💰 Salary Tracking

* Store driver salary details
* Can be extended to auto calculate salary using attendance

### ⛽ Fuel Management

* Record fuel usage for vehicles

### 🔧 Maintenance Records

* Track vehicle maintenance

### 📊 Excel Export

* Download driver attendance as **Excel file**

---

# 🛠️ Tech Stack

## Frontend

* HTML
* CSS
* JavaScript

## Backend

* Python
* FastAPI

## Database

* PostgreSQL

## Deployment

* Frontend → Vercel
* Backend → Render
* Database → Supabase PostgreSQL

---

# 📂 Project Structure

```
transport-system
│
├── api
│   └── main.py
│
├── frontend
│   ├── login.html
│   ├── dashboard.html
│   ├── vehicles.html
│   ├── drivers.html
│   ├── trips.html
│   ├── fuel.html
│   ├── maintenance.html
│   ├── salary.html
│   ├── attendance.html
│   ├── style.css
│   └── script.js
│
├── requirements.txt
└── README.md
```

---

# ⚙️ Local Setup (Optional)

If you want to run the project locally.

## 1️⃣ Clone the Repository

```
git clone https://github.com/sowndaryasree/transport-system.git
cd transport-system
```

---

## 2️⃣ Install Dependencies

```
pip install fastapi uvicorn psycopg2 pandas openpyxl
```

---

## 3️⃣ Run Backend Server

```
uvicorn main:app --reload
```

Server will start at:

```
http://127.0.0.1:8000
```

API Docs:

```
http://127.0.0.1:8000/docs
```

---

# 📊 Attendance System

The attendance system works using a **calendar interface**.

Each day can be toggled through 3 states:

| Status  | Meaning          |
| ------- | ---------------- |
| Present | Full working day |
| Half    | Half working day |
| Absent  | No work          |

Attendance is saved to the database and displayed when reopening the page.

---

# 📥 Export Attendance to Excel

Users can download attendance reports using the **Download Excel** button.

The backend generates an Excel file and sends it to the browser.

Endpoint:

```
/download_attendance
```

---

# 🔐 Login System

The project uses a simple login check:

```
localStorage.setItem("loggedIn","true")
```

If the user is not logged in, pages redirect to the login screen.

---

# 🚀 Future Improvements

Possible upgrades for the system:

* Role based authentication (Admin / Staff)
* Driver salary auto calculation
* Attendance analytics dashboard
* Route management
* Mobile responsive design
* Email report generation
* Vehicle GPS tracking integration

---

# 👩‍💻 Author

Sowndaryasree

---

# 📄 License

This project is created for educational purposes and academic demonstration.

const API = "https://transport-system-1-i84e.onrender.com";

// --- EXCEL DOWNLOAD (FIXED) ---
function exportReport() {
    // This points to the correct endpoint. 
    // If your backend uses a different name, change "export_report" below.
    window.location.href = API + "/export_report"; 
}

// VEHICLES
function addVehicle(){
    let name = document.getElementById("vehicle_name").value;
    let number = document.getElementById("vehicle_number").value;
    let type = document.getElementById("vehicle_type").value;
    let unit = document.getElementById("unit_capacity").value;

    fetch(API+"/add_vehicle?vehicle_name="+name+
    "&vehicle_number="+number+
    "&vehicle_type="+type+
    "&unit_capacity="+unit,{
    method:"POST"
    })
    .then(res=>res.json())
    .then(()=>{
    alert("Vehicle Added");
    loadVehicles();
    });
}

function loadVehicles(){
    fetch(API+"/get_vehicles")
    .then(res=>res.json())
    .then(data=>{
    let table=document.getElementById("vehicle_table");
    table.innerHTML=`
    <tr>
    <th>Name</th>
    <th>Number</th>
    <th>Type</th>
    <th>Unit</th>
    <th>Edit</th>
    </tr>
    `;
    data.forEach(v=>{
    table.innerHTML+=`
    <tr>
    <td>${v.vehicle_name}</td>
    <td>${v.vehicle_number}</td>
    <td>${v.vehicle_type}</td>
    <td>${v.unit_capacity}</td>
    <td><button onclick="editVehicle('${v.id}','${v.vehicle_name}','${v.vehicle_number}','${v.vehicle_type}','${v.unit_capacity}')">Edit</button></td>
    </tr>
    `;
    });
    });
}

// Fixed missing editVehicle logic
function editVehicle(id, name, number, type, unit) {
    document.getElementById("vehicle_name").value = name;
    document.getElementById("vehicle_number").value = number;
    document.getElementById("vehicle_type").value = type;
    document.getElementById("unit_capacity").value = unit;
    window.currentVehicle = id;
}

loadVehicles();

// DRIVERS
function addDriver(){
    let name=document.getElementById("driver_name").value;
    let phone=document.getElementById("driver_phone").value;
    let license=document.getElementById("license_number").value;

    fetch(API+"/add_driver?name="+name+
    "&phone="+phone+
    "&license_number="+license,{
    method:"POST"
    })
    .then(res=>res.json())
    .then(()=>{
    alert("Driver Added");
    loadDrivers();
    });
}

function loadDrivers(){
    fetch(API+"/get_drivers")
    .then(res=>res.json())
    .then(data=>{
    let table=document.getElementById("driver_table");
    table.innerHTML=`
    <tr>
    <th>Name</th>
    <th>Phone</th>
    <th>License</th>
    <th>Edit</th>
    </tr>
    `;
    data.forEach(d=>{
    table.innerHTML+=`
    <tr>
    <td>${d.name}</td>
    <td>${d.phone}</td>
    <td>${d.license_number}</td>
    <td><button onclick="editDriver('${d.id}','${d.name}','${d.phone}','${d.license_number}')">Edit</button></td>
    </tr>
    `;
    });
    });
}

function editDriver(id, name, phone, license) {
    document.getElementById("driver_name").value = name;
    document.getElementById("driver_phone").value = phone;
    document.getElementById("license_number").value = license;
    window.currentDriver = id;
}

loadDrivers();

// TRIPS
function addTrip(){
    let vehicle=document.getElementById("trip_vehicle").value;
    let driver=document.getElementById("trip_driver").value;
    let material=document.getElementById("material_type").value;
    let units=document.getElementById("trip_units").value;
    let loading=document.getElementById("loading_location").value;
    let delivery=document.getElementById("delivery_location").value;
    let customer=document.getElementById("trip_customer").value;
    let loading_cost=document.getElementById("loading_cost").value;
    let payment=document.getElementById("customer_payment").value;
    let start_date=document.getElementById("start_date").value;
    let end_date=document.getElementById("end_date").value;
    let start=document.getElementById("start_time").value;
    let end=document.getElementById("end_time").value;

    fetch(API+"/add_trip?vehicle="+vehicle+
    "&driver="+driver+
    "&material_type="+material+
    "&units="+units+
    "&loading_location="+loading+
    "&delivery_location="+delivery+
    "&customer="+customer+
    "&loading_cost="+loading_cost+
    "&customer_payment="+payment+
    "&start_date="+start_date+
    "&end_date="+end_date+
    "&start_time="+start+
    "&end_time="+end,{
    method:"POST"
    })
    .then(res=>res.json())
    .then(()=>{
    alert("Trip Added");
    loadTrips();
    });
}

function loadTrips(){
    fetch(API+"/get_trips")
    .then(res=>res.json())
    .then(data=>{
    let table=document.getElementById("trip_table");
    table.innerHTML=`
    <tr>
    <th>Vehicle</th>
    <th>Driver</th>
    <th>Material</th>
    <th>Units</th>
    <th>Customer</th>
    <th>Payment</th>
    <th>Edit</th>
    </tr>
    `;
    data.forEach(t=>{
    table.innerHTML+=`
    <tr>
    <td>${t.vehicle}</td>
    <td>${t.driver}</td>
    <td>${t.material_type}</td>
    <td>${t.units}</td>
    <td>${t.customer}</td>
    <td>${t.customer_payment}</td>
    <td><button onclick="editTrip('${t.id}','${t.vehicle}','${t.driver}','${t.material_type}','${t.units}','${t.customer}','${t.customer_payment}')">Edit</button></td>
    </tr>
    `;
    });
    });
}

function editTrip(id, vehicle, driver, material, units, customer, payment) {
    document.getElementById("trip_vehicle").value = vehicle;
    document.getElementById("trip_driver").value = driver;
    document.getElementById("material_type").value = material;
    document.getElementById("trip_units").value = units;
    document.getElementById("trip_customer").value = customer;
    document.getElementById("customer_payment").value = payment;
    window.currentTrip = id;
}

loadTrips();

// FUEL
function addFuel(){
    let vehicle=document.getElementById("fuel_vehicle").value;
    let type=document.getElementById("fuel_type").value;
    let litres=document.getElementById("fuel_litres").value;
    let rate=document.getElementById("fuel_rate").value;
    let station=document.getElementById("fuel_station").value;
    let date=document.getElementById("fuel_date").value;

    fetch(API+"/add_fuel?vehicle="+vehicle+
    "&fuel_type="+type+
    "&litres="+litres+
    "&rate="+rate+
    "&station="+station+
    "&fuel_date="+date,{
    method:"POST"
    })
    .then(()=>{
    alert("Fuel Added");
    loadFuel();
    });
}

function loadFuel(){
    fetch(API+"/get_fuel")
    .then(res=>res.json())
    .then(data=>{
    let table=document.getElementById("fuel_table");
    table.innerHTML=`
    <tr>
    <th>Vehicle</th>
    <th>Type</th>
    <th>Litres</th>
    <th>Rate</th>
    <th>Total</th>
    <th>Station</th>
    <th>Edit</th>
    </tr>
    `;
    data.forEach(f=>{
    table.innerHTML+=`
    <tr>
    <td>${f.vehicle}</td>
    <td>${f.fuel_type}</td>
    <td>${f.litres}</td>
    <td>${f.rate}</td>
    <td>${f.total_cost}</td>
    <td>${f.station}</td>
    <td><button onclick="editFuel('${f.id}','${f.vehicle}','${f.fuel_type}','${f.litres}','${f.rate}','${f.station}','${f.fuel_date}')">Edit</button></td>
    </tr>
    `;
    });
    });
}

loadFuel();

// SALARY
function addSalary(){
    let driver=document.getElementById("salary_driver").value;
    let amount=document.getElementById("salary_amount").value;
    let notes=document.getElementById("salary_notes").value;
    let date=document.getElementById("salary_date").value;

    fetch(API+"/add_salary?driver_name="+driver+
    "&amount="+amount+
    "&notes="+notes+
    "&salary_date="+date,{
    method:"POST"
    })
    .then(()=>{
    alert("Salary Added");
    loadSalary();
    });
}

function loadSalary(){
    fetch(API+"/get_salary")
    .then(res=>res.json())
    .then(data=>{
    let table=document.getElementById("salary_table");
    table.innerHTML=`
    <tr>
    <th>Driver</th>
    <th>Amount</th>
    <th>Notes</th>
    <th>Edit</th>
    </tr>
    `;
    data.forEach(s=>{
    table.innerHTML+=`
    <tr>
    <td>${s.driver_name}</td>
    <td>${s.amount}</td>
    <td>${s.notes}</td>
    <td><button onclick="editSalary('${s.id}','${s.driver_name}','${s.amount}','${s.notes}','${s.salary_date}')">Edit</button></td>
    </tr>
    `;
    });
    });
}

loadSalary();

// EDIT FUEL (Logic)
function editFuel(id,vehicle,type,litres,rate,station,date){
    document.getElementById("fuel_vehicle").value=vehicle
    document.getElementById("fuel_type").value=type
    document.getElementById("fuel_litres").value=litres
    document.getElementById("fuel_rate").value=rate
    document.getElementById("fuel_station").value=station
    document.getElementById("fuel_date").value=date
    window.currentFuel=id
}

function updateFuel(){
    let vehicle=document.getElementById("fuel_vehicle").value
    let type=document.getElementById("fuel_type").value
    let litres=document.getElementById("fuel_litres").value
    let rate=document.getElementById("fuel_rate").value
    let station=document.getElementById("fuel_station").value
    let date=document.getElementById("fuel_date").value

    fetch(API+"/update_fuel/"+window.currentFuel+
    "?vehicle="+vehicle+
    "&fuel_type="+type+
    "&litres="+litres+
    "&rate="+rate+
    "&station="+station+
    "&fuel_date="+date,{
    method:"PUT"
    })
    .then(()=>{
    alert("Fuel Updated")
    loadFuel()
    })
}

// EDIT SALARY (Logic)
function editSalary(id,driver,amount,notes,date){
    document.getElementById("salary_driver").value=driver
    document.getElementById("salary_amount").value=amount
    document.getElementById("salary_notes").value=notes
    document.getElementById("salary_date").value=date
    window.currentSalary=id
}

function updateSalary(){
    let driver=document.getElementById("salary_driver").value
    let amount=document.getElementById("salary_amount").value
    let notes=document.getElementById("salary_notes").value
    let date=document.getElementById("salary_date").value

    fetch(API+"/update_salary/"+window.currentSalary+
    "?driver_name="+driver+
    "&amount="+amount+
    "&notes="+notes+
    "&salary_date="+date,{
    method:"PUT"
    })
    .then(()=>{
    alert("Salary Updated")
    loadSalary()
    })
}
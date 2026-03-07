const API = "https://transport-system-seven.vercel.app/api";

function addVehicle(){

let name = document.getElementById("vehicle_name").value;
let number = document.getElementById("vehicle_number").value;
let type = document.getElementById("vehicle_type").value;
let unit = document.getElementById("unit_capacity").value;

fetch(API + "/add_vehicle?vehicle_name="+name+
"&vehicle_number="+number+
"&vehicle_type="+type+
"&unit_capacity="+unit,{
method:"POST"
})
.then(res=>res.json())
.then(data=>{
alert("Vehicle Added");
loadVehicles();
});

}

function loadVehicles(){

fetch("https://transport-system-seven.vercel.app/api/get_vehicles")
.then(res => res.json())
.then(data => {

let table = document.getElementById("vehicle_table");

table.innerHTML = `
<tr>
<th>Name</th>
<th>Number</th>
<th>Type</th>
<th>Unit</th>
</tr>
`;

data.forEach(v => {

let row = `
<tr>
<td>${v.vehicle_name}</td>
<td>${v.vehicle_number}</td>
<td>${v.vehicle_type}</td>
<td>${v.unit_capacity}</td>
</tr>
`;

table.innerHTML += row;

});

});

}
loadVehicles();

function addDriver(){

let name = document.getElementById("driver_name").value;
let phone = document.getElementById("driver_phone").value;
let license = document.getElementById("license_number").value;

fetch("https://transport-system-seven.vercel.app/api/add_driver?name="+name+
"&phone="+phone+
"&license_number="+license,{
method:"POST"
})
.then(res=>res.json())
.then(data=>{
alert("Driver Added");
loadDrivers();
});

}



function loadDrivers(){

fetch("https://transport-system-seven.vercel.app/api/get_drivers")
.then(res=>res.json())
.then(data=>{

let table = document.getElementById("driver_table");

table.innerHTML = `
<tr>
<th>Name</th>
<th>Phone</th>
<th>License</th>
</tr>
`;

data.forEach(d=>{

table.innerHTML += `
<tr>
<td>${d.name}</td>
<td>${d.phone}</td>
<td>${d.license_number}</td>
</tr>
`;

});

});

}
loadDrivers();
function addTrip(){

let vehicle = document.getElementById("trip_vehicle").value;
let driver = document.getElementById("trip_driver").value;
let material = document.getElementById("material_type").value;
let units = document.getElementById("trip_units").value;
let loading = document.getElementById("loading_location").value;
let delivery = document.getElementById("delivery_location").value;
let customer = document.getElementById("trip_customer").value;
let loading_cost = document.getElementById("loading_cost").value;
let payment = document.getElementById("customer_payment").value;
let date = document.getElementById("trip_date").value
let start = document.getElementById("start_time").value
let end = document.getElementById("end_time").value
fetch("https://transport-system-seven.vercel.app/api/add_trip?vehicle="+vehicle+
"&driver="+driver+
"&material_type="+material+
"&units="+units+
"&loading_location="+loading+
"&delivery_location="+delivery+
"&customer="+customer+
"&loading_cost="+loading_cost+
"&customer_payment="+payment+
"&trip_date="+date+
"&start_time="+start+
"&end_time="+end,{
method:"POST"
})
.then(res=>res.json())
.then(data=>{
alert("Trip Added");
loadTrips();
});

}



function loadTrips(){

fetch("https://transport-system-seven.vercel.app/api/get_trips")
.then(res=>res.json())
.then(data=>{

let table = document.getElementById("trip_table");

table.innerHTML = `
<tr>
<th>Vehicle</th>
<th>Driver</th>
<th>Material</th>
<th>Units</th>
<th>Customer</th>
<th>Payment</th>
</tr>
`;

data.forEach(t=>{

table.innerHTML += `
<tr>
<td>${t.vehicle}</td>
<td>${t.driver}</td>
<td>${t.material_type}</td>
<td>${t.units}</td>
<td>${t.customer}</td>
<td>${t.customer_payment}</td>
</tr>
`;

});

});

}

loadTrips();

function addFuel(){

let vehicle = document.getElementById("fuel_vehicle").value;
let type = document.getElementById("fuel_type").value;
let litres = document.getElementById("fuel_litres").value;
let rate = document.getElementById("fuel_rate").value;
let station = document.getElementById("fuel_station").value;
let date = document.getElementById("fuel_date").value
fetch(API + "/add_fuel?vehicle="+vehicle+
"&fuel_type="+type+
"&litres="+litres+
"&rate="+rate+
"&station="+station+
"&fuel_date="+date,{
method:"POST"
})
.then(res=>res.json())
.then(data=>{
alert("Fuel Added");
loadFuel();
});

}



function loadFuel(){

fetch("https://transport-system-seven.vercel.app/api/get_fuel")
.then(res=>res.json())
.then(data=>{

let table = document.getElementById("fuel_table");

table.innerHTML = `
<tr>
<th>Vehicle</th>
<th>Type</th>
<th>Litres</th>
<th>Rate</th>
<th>Total</th>
<th>Station</th>
</tr>
`;

data.forEach(f=>{

table.innerHTML += `
<tr>
<td>${f.vehicle}</td>
<td>${f.fuel_type}</td>
<td>${f.litres}</td>
<td>${f.rate}</td>
<td>${f.total_cost}</td>
<td>${f.station}</td>
</tr>
`;

});

});

}

loadFuel();

function addMaintenance(){

let vehicle = document.getElementById("maint_vehicle").value;
let type = document.getElementById("maint_type").value;
let cost = document.getElementById("maint_cost").value;
let workshop = document.getElementById("maint_workshop").value;
let date = document.getElementById("maintenance_date").value
fetch(API + "/add_maintenance?vehicle="+vehicle+
"&maintenance_type="+type+
"&cost="+cost+
"&workshop="+workshop+
"&maintenance_date="+date,{
method:"POST"
})
.then(res=>res.json())
.then(data=>{
alert("Maintenance Added");
loadMaintenance();
});

}



function loadMaintenance(){

fetch("https://transport-system-seven.vercel.app/api/get_maintenance")
.then(res=>res.json())
.then(data=>{

let table = document.getElementById("maintenance_table");

table.innerHTML = `
<tr>
<th>Vehicle</th>
<th>Type</th>
<th>Cost</th>
<th>Workshop</th>
</tr>
`;

data.forEach(m=>{

table.innerHTML += `
<tr>
<td>${m.vehicle}</td>
<td>${m.maintenance_type}</td>
<td>${m.cost}</td>
<td>${m.workshop}</td>
</tr>
`;

});

});

}

loadMaintenance();
function addSalary(){

let driver = document.getElementById("salary_driver").value;
let amount = document.getElementById("salary_amount").value;
let notes = document.getElementById("salary_notes").value;

fetch("https://transport-system-seven.vercel.app/api/add_salary?driver_name="+driver+
"&amount="+amount+
"&notes="+notes,{
method:"POST"
})
.then(res=>res.json())
.then(data=>{
alert("Salary Added");
loadSalary();
});
let date = document.getElementById("salary_date").value

fetch(API + "/add_salary?driver_name="+driver+
"&amount="+amount+
"&notes="+notes+
"&salary_date="+date,{
method:"POST"
})

}



function loadSalary(){

fetch("https://transport-system-seven.vercel.app/api/get_salary")
.then(res=>res.json())
.then(data=>{

let table = document.getElementById("salary_table");

table.innerHTML = `
<tr>
<th>Driver</th>
<th>Amount</th>
<th>Notes</th>
</tr>
`;

data.forEach(s=>{

table.innerHTML += `
<tr>
<td>${s.driver_name}</td>
<td>${s.amount}</td>
<td>${s.notes}</td>
</tr>
`;

});

});

}

loadSalary();

function loadDashboard(){

Promise.all([
fetch("https://transport-system-seven.vercel.app/api/get_trips").then(r=>r.json()),
fetch("https://transport-system-seven.vercel.app/api/get_fuel").then(r=>r.json()),
fetch("https://transport-system-seven.vercel.app/api/get_maintenance").then(r=>r.json()),
fetch("https://transport-system-seven.vercel.app/api/get_salary").then(r=>r.json())
])
.then(([trips,fuel,maintenance,salary])=>{

let totalTrips = trips.length;

let income = 0;
trips.forEach(t=>{
income += t.customer_payment;
});

let fuelCost = 0;
fuel.forEach(f=>{
fuelCost += f.total_cost;
});

let maintenanceCost = 0;
maintenance.forEach(m=>{
maintenanceCost += m.cost;
});

let salaryCost = 0;
salary.forEach(s=>{
salaryCost += s.amount;
});

let profit = income - fuelCost - maintenanceCost - salaryCost;

document.getElementById("total_trips").innerText = totalTrips;
document.getElementById("total_income").innerText = income;
document.getElementById("fuel_expense").innerText = fuelCost;
document.getElementById("maintenance_expense").innerText = maintenanceCost;
document.getElementById("salary_expense").innerText = salaryCost;
document.getElementById("profit").innerText = profit;

});

}

loadDashboard();
function downloadExcel(){

window.open("https://transport-system-seven.vercel.app/api/export_excel")

}

function markAttendance(){

let driver=document.getElementById("driver").value
let date=document.getElementById("date").value
let status=document.getElementById("status").value

fetch("https://transport-system-seven.vercel.app/api/add_attendance?driver_name="+driver+"&date="+date+"&status="+status,{
method:"POST"
})

.then(()=>{

alert("Attendance saved")

})

}

function downloadFuel() {
    window.open("https://transport-system-seven.vercel.app/api/export_fuel_excel");
}

function downloadSalary() {
    window.open("https://transport-system-seven.vercel.app/api/export_salary_excel");
}

function downloadMaintenance() {
    window.open("https://transport-system-seven.vercel.app/api/export_maintenance_excel");
}
function logout(){

    localStorage.removeItem("loggedIn")
    window.location.href = "login.html"

}

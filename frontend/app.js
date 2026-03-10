const API = "https://transport-system-1-i84e.onrender.com";

/* ------------------ EXCEL DOWNLOAD ------------------ */

function exportReport(){
    window.open(API + "/download_attendance");
}

/* ------------------ VEHICLES ------------------ */

function addVehicle(){
    let name=document.getElementById("vehicle_name").value;
    let number=document.getElementById("vehicle_number").value;
    let type=document.getElementById("vehicle_type").value;
    let unit=document.getElementById("unit_capacity").value;

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
        if(!table) return;

        table.innerHTML=`
        <tr>
        <th>Name</th>
        <th>Number</th>
        <th>Type</th>
        <th>Unit</th>
        </tr>
        `;

        data.forEach(v=>{
            table.innerHTML+=`
            <tr>
            <td>${v.vehicle_name}</td>
            <td>${v.vehicle_number}</td>
            <td>${v.vehicle_type}</td>
            <td>${v.unit_capacity}</td>
            </tr>
            `;
        });
    });
}

loadVehicles();

/* ------------------ DRIVERS ------------------ */

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
        if(!table) return;

        table.innerHTML=`
        <tr>
        <th>Name</th>
        <th>Phone</th>
        <th>License</th>
        </tr>
        `;

        data.forEach(d=>{
            table.innerHTML+=`
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

/* ------------------ TRIPS ------------------ */

function addTrip(){

let vehicle=document.getElementById("trip_vehicle").value;
let driver=document.getElementById("trip_driver").value;
let material=document.getElementById("material_type").value;
let units=document.getElementById("trip_units").value;
let customer=document.getElementById("trip_customer").value;
let payment=document.getElementById("customer_payment").value;

fetch(API+"/add_trip?vehicle="+vehicle+
"&driver="+driver+
"&material_type="+material+
"&units="+units+
"&customer="+customer+
"&customer_payment="+payment,{
method:"POST"
})
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
if(!table) return;

table.innerHTML=`
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
table.innerHTML+=`
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

/* ------------------ FUEL ------------------ */

function addFuel(){

let vehicle=document.getElementById("fuel_vehicle").value;
let type=document.getElementById("fuel_type").value;
let litres=document.getElementById("fuel_litres").value;
let rate=document.getElementById("fuel_rate").value;

fetch(API+"/add_fuel?vehicle="+vehicle+
"&fuel_type="+type+
"&litres="+litres+
"&rate="+rate,{
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
if(!table) return;

table.innerHTML=`
<tr>
<th>Vehicle</th>
<th>Fuel</th>
<th>Litres</th>
<th>Rate</th>
<th>Total</th>
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
</tr>
`;
});

});

}

loadFuel();
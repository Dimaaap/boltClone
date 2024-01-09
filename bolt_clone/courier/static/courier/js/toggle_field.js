let cities = document.querySelectorAll(".country-select");
const fleetLabel = document.getElementById("fleet-label");
const fleetSmall = document.getElementById("fleet-small");
const courierFleet = document.getElementById("id_courier_fleet");
const fleetDesc = document.querySelectorAll(".fleet-desc");

cities.forEach(function(city) {
    city.addEventListener("change", function() {
        let isKyivSelected = cities[1].checked;

        fleetLabel.style.display = isKyivSelected ? "inline-block" : "none";
        fleetSmall.style.display = isKyivSelected ? "inline-block" : "none";
        courierFleet.style.display = isKyivSelected ? "flex" : "none";
        fleetDesc.forEach((paragraph) => {
            if(isKyivSelected) {
                paragraph.style.display = "block";
            } else {
                paragraph.style.display = "none";
            }
        })
    });
});



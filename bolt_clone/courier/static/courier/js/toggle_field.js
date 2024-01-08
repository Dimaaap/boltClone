let cityCheckboxes = document.getElementById("id_courier_city");
let fleetCheckboxes = document.getElementById("id_courier_fleet");

cityCheckboxes.forEach((checkbox) => {
    checkbox.addEventListener('change', () => {
        let atLeastOneCitySelected = Array.from(cityCheckboxes).some((cityCheckboxes) => {
            return cityCheckboxes.checked && cityCheckboxes.value === "Київ";
        });

        fleetCheckboxes
    })
})
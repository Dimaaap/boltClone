const carBrandDropdown = document.getElementById("car-model-select");
const carDropdown = document.getElementById("")


document.addEventListener("DOMContentLoaded", () => {
    let isCarBrandOpen = carBrandDropdown.style.display == "block";
    let isCarModelSelectOpen = carModelSelectDropdown.style.display == "block";
    console.log(isCarModelSelectOpen.style.display)
    console.log(isCarBrandOpen.style.display)
    if(isCarBrandOpen && isCarModelSelectOpen){
        carModelSelectDropdown.style.display = "none";
    }
})
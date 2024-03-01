const carModelSelectDropdown = document.getElementById("model-select");
const carModelSelectDropdownField = document.getElementById("driver-model-car-select");
const carModelSelectChevron = Array.from(document.querySelectorAll(".fa-angle-down"))[1];
const carModalFaXMark = Array.from(document.querySelectorAll(".fa-xmark"))[1];
const carBrandField = document.getElementById("driver-car-select");


let isModalWindowOpen = false;

const showHideDropdownWindow = () => {
    if(!isModalWindowOpen){
        carModelSelectDropdown.style.display = "block";
    } else {
        carModelSelectDropdown.style.display = "none";
    }
    isModalWindowOpen = !isModalWindowOpen;
}

carModelSelectDropdownField.addEventListener("click", () => {
    showHideDropdownWindow();
})

carModelSelectChevron.addEventListener("click", () => {
    showHideDropdownWindow();
})


carBrandField.addEventListener("change", () => {
    const selectedBrand = carBrandField.value;
    carModelSelectDropdown.innerHTML = "";
    let deviceIp = "127.0.0.1"
    if(selectedBrand){

        fetch(`/driver/search_car_model/${deviceIp}/${selectedBrand}/`, {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
                "X-CSRFToken": getCookie("csrftoken")
            },
            body: JSON.stringify({"brand": selectedBrand}),
        })
        .then(response => response.json())
        .then(data => {
            data.forEach((model) => {
                const option = document.createElement("option");
                option.value = model;
                option.textContent = model;
                carModelSelectDropdown.appendChild(option)
            })
        })
        .catch(error => console.error("Error fetching car models: " + error))
    }
})
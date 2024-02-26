const driverHasOwnCar = document.getElementById("id_has_own_car");
const driverNoHasOwnCarLabel = document.getElementById("second-checkbox");
const driverNoHasOwnCar = document.getElementById("id_no_has_own_car");
let fieldsAfterCheckboxes = Array.from(document.querySelectorAll(".after-checkboxes"));
const notFoundCarSmall = document.querySelector(".not-found-car-model");
const xMarkSpansList = document.querySelectorAll(".xmark-span");
const driverCarModelSelectField = document.getElementById("driver-model-car-select")


console.log(fieldsAfterCheckboxes)

document.addEventListener("DOMContentLoaded", () => {
    handleSecondCheckboxVisibility();
    driverHasOwnCar.addEventListener("change", () => {
        handleSecondCheckboxVisibility();
    })

    function handleSecondCheckboxVisibility() {
        if(driverHasOwnCar.checked){
            driverNoHasOwnCarLabel.style.display = "none";
            driverNoHasOwnCar.style.display = "none";
            fieldsAfterCheckboxes.forEach((input) => {
                input.style.display = "inline-block";
            })
            notFoundCarSmall.style.display = "block";
            xMarkSpansList.forEach((xMark) => {
                xMark.style.display = "flex";
            })
            driverCarModelSelectField.style.display = "none";
            xMarkSpansList[1].style.display = "none";
        } else {
            driverNoHasOwnCarLabel.style.display = "inline-block";
            driverNoHasOwnCar.style.display = "inline-block";
            fieldsAfterCheckboxes.forEach((input) => {
                input.style.display = "none";
            })
            notFoundCarSmall.style.display = "none";
            xMarkSpansList.forEach((xMark) => {
                xMark.style.display = "none";
            })
        }
    }
});
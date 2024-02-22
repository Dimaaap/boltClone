const driverHasOwnCar = document.getElementById("id_has_own_car");
const driverNoHasOwnCarLabel = document.getElementById("second-checkbox");
const driverNoHasOwnCar = document.getElementById("id_no_has_own_car");
let fieldsAfterCheckboxes = Array.from(document.querySelectorAll(".after-checkboxes"))

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
        } else {
            driverNoHasOwnCarLabel.style.display = "inline-block";
            driverNoHasOwnCar.style.display = "inline-block";
            fieldsAfterCheckboxes.forEach((input) => {
                input.style.display = "none";
            })
        }
    }
});
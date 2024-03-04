const yearSelectField = document.getElementById("created-car-year-select-field")
const yearSelectDropdown = document.getElementById("year-select")
const yearArrow = Array.from(document.querySelectorAll(".fa-angle-down"))[2]
const yearSelectDropdownOptions = yearSelectDropdown.querySelectorAll("p");
const yearXMark = Array.from(document.querySelectorAll(".fa-xmark"))[2]

let isYearModalWindowOpen = false;

const showHideYearDropdownWindow = () => {
    if(!isYearModalWindowOpen){
        yearSelectDropdown.style.display = "block";
    } else {
        yearSelectDropdown.style.display = "none";
    }
    isYearModalWindowOpen = !isYearModalWindowOpen;
}


yearSelectField.addEventListener("click", () => {
    showHideYearDropdownWindow();
})

yearArrow.addEventListener("click", () => {
    showHideYearDropdownWindow();
})

yearSelectDropdownOptions.forEach((year) => {
    year.addEventListener("click", () => {
        yearSelectField.value = year.innerText;
        showHideYearDropdownWindow();
        yearXMark.style.display = "flex";
    })
})
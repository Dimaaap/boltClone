const colorSelectField = document.getElementById("form-car-color-select-field");
const colorSelectDropdown = document.getElementById("color-select");
const colorArrow = Array.from(document.querySelectorAll(".fa-angle-down"))[3]
const colorXMark = Array.from(document.querySelectorAll(".fa-xmark"))[3]
const colorSelectDropdownOptions = colorSelectDropdown.querySelectorAll("p")

let isColorSelectOpen = false;


const showHideColorDropdown = () => {
    if(!isColorSelectOpen){
        colorSelectDropdown.style.display = "block";
    } else {
        colorSelectDropdown.style.display = "none";
    }
    isColorSelectOpen = !isColorSelectOpen;
}


colorSelectField.addEventListener("click", () => {
    showHideColorDropdown();
})

colorArrow.addEventListener("click", () => {
    showHideColorDropdown();
})

colorSelectDropdownOptions.forEach((color) => {
    color.addEventListener("click", () => {
        colorSelectField.value = color.innerText;
        showHideColorDropdown();
        colorXMark.style.display = "flex";
    })
})
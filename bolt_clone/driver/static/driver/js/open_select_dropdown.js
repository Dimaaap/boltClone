const selectField = document.getElementById("city-select-field");
const hideDropdownBtn = document.getElementById("open-dropdown");
const dropdown = document.getElementById("dropdown");
const iconsRow = document.querySelector(".icons");
const citySelectField = document.getElementById("city-select-field");

let modalIsOpen = false;
let iconsRowInitialTop;

hideDropdownBtn.addEventListener("click", () => {
    if(!modalIsOpen){
        dropdown.style.display = "block";
        iconsRow.style.top = "30%";

    } else {
        dropdown.style.display = "none";
        iconsRow.style.top = iconsRowInitialTop;
    }
    modalIsOpen = !modalIsOpen
})

citySelectField.addEventListener("focus", () => {
    if(!modalIsOpen){
        dropdown.style.display = "block";
        iconsRow.style.top = "30%";
    } else {
        dropdown.style.display = "none";
        iconsRow.style.top = iconsRowInitialTop;
    }

    modalIsOpen = !modalIsOpen;
})

document.addEventListener("DOMContentLoaded", () => {
    iconsRowInitialTop = iconsRow.style.top;
})
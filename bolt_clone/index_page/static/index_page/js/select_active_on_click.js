const selectInput = document.querySelector(".main-content form select");
const icon = document.querySelector(".main-content form i");
const selectCuisineInput = document.getElementById("cuisine-choice")
const selectCuisineArrow = document.getElementById("bottom-arrow");
const selectCountryCodeInput = document.getElementById("id_country_phone_code");
const selectCountryCodeArrow = document.getElementById("bottom-arrow-down");

let isIconRotated = false;
let isBottomRotated = false;
let isDownArrowRotated = false;

selectCountryCodeInput.addEventListener("click", () => {
    isDownArrowRotated = !isDownArrowRotated;
    selectCountryCodeArrow.style.transform = isDownArrowRotated ? "rotate(180deg)" : "";
    selectCountryCodeArrow.style.transformOrigin = isDownArrowRotated ? "50% 20%" : "";
})

selectCuisineInput.addEventListener("click", () => {
    isBottomRotated = !isBottomRotated;
    selectCuisineArrow.style.transform = isBottomRotated ? "rotate(180deg)" : "";
    selectCuisineArrow.style.transformOrigin = isBottomRotated ? "50% 20%": "";
})

selectInput.addEventListener("click", () => {
    isIconRotated = !isIconRotated;
    icon.style.transform = isIconRotated ? "rotate(180deg)" : "";
    icon.style.transformOrigin = isIconRotated ? "50% 20%" : "";
})
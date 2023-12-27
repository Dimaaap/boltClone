const nicheField = document.getElementById("id_partner_niche");
const cuisineField = document.querySelector(".conditional-field");
const countryPhoneCodeField = document.getElementById("id_country_phone_code");
const countryPhoneCodeArrow = document.getElementById("bottom-arrow-down");
const selectNicheArrow = document.getElementById("select-niche-arrow");

let currentCountryPhonePos = parseInt(getComputedStyle(countryPhoneCodeField).top, 10)
let currentSelectNichePos = parseInt(getComputedStyle(selectNicheArrow).top, 10);


nicheField.addEventListener("change", () => {
    if(nicheField.value !== "Заклад харчування") {
        cuisineField.style.display = 'none';
        let newPos = currentCountryPhonePos - 100;
        countryPhoneCodeField.style.top = newPos + "px";
        let newPosArr = currentCountryPhonePos - 236;
        countryPhoneCodeArrow.style.top = newPosArr + "px";
        let newNicheArr = currentSelectNichePos + 2;
        selectNicheArrow.style.top = newNicheArr + "px";
    } else {
        cuisineField.style.display = 'block';
        let newPos = currentCountryPhonePos + 0;
        countryPhoneCodeField.style.top = newPos + "px";
        let newPosArr = currentCountryPhonePos + 25;
        countryPhoneCodeArrow.style.top = newPosArr + "px";
    }
})
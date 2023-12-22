const nicheField = document.getElementById("id_partner_niche");
const cuisineField = document.querySelector(".conditional-field");
const countryPhoneCodeField = document.getElementById("id_country_phone_code");
const countryPhoneCodeArrow = document.getElementById("bottom-arrow-down");
const selectNicheArrow = document.querySelector()

let currentCountryPhonePos = parseInt(getComputedStyle(countryPhoneCodeField).top, 10)


nicheField.addEventListener("change", () => {
    if(nicheField.value !== "Заклад харчування") {
        cuisineField.style.display = 'none';
        let newPos = currentCountryPhonePos - 100;
        countryPhoneCodeField.style.top = newPos + "px";
        let newPosArr = currentCountryPhonePos - 75;
        countryPhoneCodeArrow.style.top = newPosArr + "px";
    } else {
        cuisineField.style.display = 'block';
        let newPos = currentCountryPhonePos + 0;
        countryPhoneCodeField.style.top = newPos + "px";
        let newPosArr = currentCountryPhonePos + 25;
        countryPhoneCodeArrow.style.top = newPosArr + "px";
    }
})
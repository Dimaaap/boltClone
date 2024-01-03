const conditionalFields = document.querySelectorAll(".conditional-field.error");
const countryCodeField = document.querySelectorAll(".select-country-flag");

let phoneNumberField = null;
for(const field of conditionalFields){
    if(field.id === "phone-number-container"){
        phoneNumberField = field;
    }
}

if (phoneNumberField){
    console.log(countryCodeField);
    countryCodeField.style.top = 50 + "px";
    console.log(currentCountryPhonePos);
}
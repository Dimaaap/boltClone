const form = document.querySelector("form");
const hiddenField = document.getElementById("other-company_field");
const rentCompanyField = document.getElementById("id_rent_company");
const hiddenBlock = document.querySelector(".hidden");
const rentCompanyOptions = Array.from(document.querySelectorAll("option"))

hiddenBlock.style.display = "none";

rentCompanyField.addEventListener("change", () => {
    let selectedValue = rentCompanyField.value;
    if(selectedValue === "Інше"){
        hiddenBlock.style.display = "block"
    } else {
        hiddenBlock.style.display = "none";
    }
})

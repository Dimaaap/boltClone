const otherReportForm = document.getElementById("other-report-form");
const hidden_field = document.getElementById("other_company_field_other_report");
const otherRentCompanyField = document.getElementById("second-rent-company");
const secondHiddenBlock = document.getElementById("second-hidden-block");
const rentCompanyOptionsArr = Array.from(document.querySelectorAll("option"));

secondHiddenBlock.style.display = "none";

otherRentCompanyField.addEventListener("change", () => {
    let selectedValue = otherRentCompanyField.value;
    console.log(selectedValue)
    if(selectedValue === "Інше"){
        secondHiddenBlock.style.display = "block";
    } else {
        secondHiddenBlock.style.display = "none";
    }
})

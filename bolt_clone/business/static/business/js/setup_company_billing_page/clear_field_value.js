const companyNameField = document.getElementById("company-legal-name");
const clearFieldBtn = document.getElementById("inplace-icon");


companyNameField.addEventListener("mouseover", () => {
    if(companyNameField.value.length >= 1){
        clearFieldBtn.style.display = "inline-block";
    }
})


companyNameField.addEventListener("mouseout", () => {
    clearFieldBtn.style.display = "none";
})


clearFieldBtn.addEventListener("click", () => {
    companyNameField.value = ""
    clearFieldBtn.style.display = "none";
})

clearFieldBtn.addEventListener("mouseover", () => {
    clearFieldBtn.style.display = "inline-block";
})

companyNameField.addEventListener("input", () => {
    if(companyNameField.value.length <= 1){
        clearFieldBtn.style.display = "none";
    }
    else {
        clearFieldBtn.style.display = "inline-block";
    }
})
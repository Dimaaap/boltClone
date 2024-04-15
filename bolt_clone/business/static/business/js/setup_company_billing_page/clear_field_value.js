const companyNameField = document.getElementById("company-legal-name");
const clearFieldBtn = document.querySelector(".inplace-icon");

const formFields = Array.from(document.querySelectorAll("input"))
const formSpans = Array.from(document.querySelectorAll(".inplace-icon"))

formFields.splice(0, 1);
formSpans.splice(2, 1);


formFields.forEach((formField) => {
    let fieldIndex = formFields.indexOf(formField);
    formField.addEventListener("mouseover", () => {
        if(formField.value.length >= 1){
            formSpans[fieldIndex].style.display = "inline-block";
        }
    })

    formField.addEventListener("mouseout", () => {
        formSpans[fieldIndex].style.display = "none";
    })

    formField.addEventListener("input", () => {
        if(formField.value.length < 1) {
            formSpans[fieldIndex].style.display = "none";
        } else {
            formSpans[fieldIndex].style.display = "inline-block";
        }
    })
})

formSpans.forEach((formSpan) => {
    let spanIndex = formSpans.indexOf(formSpan);
    formSpan.addEventListener("click", () => {
        formFields[spanIndex].value = ""
        formSpan.style.display = "none";
    })

    formSpan.addEventListener("mouseover", () => {
        formSpan.style.display = "inline-block";
    })
})
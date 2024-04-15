const inputFields = Array.from(document.querySelectorAll("input")).slice(3)
const inputLabels = Array.from(document.querySelectorAll("label")).slice(2)


inputFields.forEach((inputField) => {
    let fieldIndex = inputFields.indexOf(inputField);
    let fieldPlaceholder = inputField.placeholder;

    inputField.addEventListener("focus", () => {
        inputLabels[fieldIndex].style.display = "inline-block";
        inputField.placeholder = "";
    })

    inputField.addEventListener("blur", () => {
        if(inputField.value.length < 1){
            inputLabels[fieldIndex].style.display = "none";
            inputField.placeholder = fieldPlaceholder;
        }
    })

})
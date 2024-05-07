const hiddenBtn = Array.from(document.querySelectorAll(".add-location"));
const radioInputs = Array.from(document.querySelectorAll(".input-radio-field"));


radioInputs.forEach(radioInput => {
    radioInput.addEventListener("change", () => {
        let inputIndex = radioInputs.indexOf(radioInput);
        let btn = hiddenBtn[inputIndex];
        hiddenBtn.forEach(button => {
            button.style.display = "none";
        })
        btn.style.display = "block";
    })
})
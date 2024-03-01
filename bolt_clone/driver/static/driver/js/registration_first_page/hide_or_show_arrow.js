const selectArrow = document.getElementById("car-model-arrow");
const fieldWithSelect = document.getElementById("driver-model-car-select");
const carModelField = document.getElementById("driver-car-select");



carModelField.addEventListener("change", () => {
    if (fieldWithSelect.style.display === "none"){
        selectArrow.style.display = "none";
    } else {
        selectArrow.style.display = "inline-block";
    }
})
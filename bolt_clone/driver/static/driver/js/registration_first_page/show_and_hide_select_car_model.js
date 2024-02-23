const carModelSelectField = document.getElementById("driver-model-car-select");
const carSelectField = document.getElementById("driver-car-select")
const carModelSelectFieldSmall = Array.from(document.querySelectorAll(".not-found-car-model"));
const xMarks = Array.from(document.querySelectorAll(".xmark-span"));
const carModelSelectPipe = document.getElementById("car-model-field-pipe");

document.addEventListener("DOMContentLoaded", () => {
   carModelSelectField.style.display = "none";
   carModelSelectFieldSmall[1].style.display = "none";
   xMarks[0].style.top = "25%";
   carModelSelectPipe.style.display = "none";

   carSelectField.addEventListener("input", () => {
        carModelSelectField.style.display = "block";
        carModelSelectFieldSmall[1].style.display = "block";
        carModelSelectFieldSmall[0].style.display = "none";
        xMarks[0].style.top = "45%";
        xMarks[1].style.top = "25%";
        carModelSelectPipe.style.display = "inline-block";
   })
})
const driverCarSelectField = document.getElementById("driver-car-select");
const driverCarSelectFieldXMark = document.querySelector(".fa-xmark");
const driverCarModelSelect = document.getElementById("driver-model-car-select");
const smallList = Array.from(document.querySelectorAll(".not-found-car-model"));
const xMarksList = Array.from(document.querySelectorAll(".xmark-span"));


driverCarSelectFieldXMark.addEventListener("click", () => {
    xMarksList[1].style.display = "none";
    driverCarModelSelect.style.display = "none";
    carModelSelectFieldSmall[0].style.display = "block";
    smallList[1].style.display = "none";
    smallList[0].style.display = "block";
    xMarksList[0].style.top = "25%";
})
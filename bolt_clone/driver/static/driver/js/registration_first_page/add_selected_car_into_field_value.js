const carField = document.getElementById("driver-car-select");
const carOptions = Array.from(document.querySelectorAll(".car-section"));
console.log(carOptions)


carOptions.forEach((carOption) => {
    console.log(carOption)
    carOption.addEventListener("click", () => {
        console.log(carOption)
        carField.value = carOption.innerText;
    })
})
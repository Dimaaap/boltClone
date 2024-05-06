let salesControlPopup = document.getElementById("sales-control");
let trackCostsCheckbox = document.getElementById("track-costs");

let isSalesPopupOpen = false;

console.log(salesControlPopup)
console.log(trackCostsCheckbox)

trackCostsCheckbox.addEventListener("change", () => {
    if(!isSalesPopupOpen) {
        salesControlPopup.style.display = "block";
    } else {
        salesControlPopup.style.display = "none"
    }
    isSalesPopupOpen = !isSalesPopupOpen;
})
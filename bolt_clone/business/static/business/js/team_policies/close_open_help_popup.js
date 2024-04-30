const openHelpPopupBtn = document.getElementById("help");
const helpPopup = document.getElementById("help-popup");
const closeHelpPopupBtn = document.getElementById("close-popup-btn");


let isHelpPopupClose = false;

openHelpPopupBtn.addEventListener("click", () => {
    helpPopup.style.display = "block";
})

closeHelpPopupBtn.addEventListener("click", () => {
    helpPopup.style.display = "none";
})
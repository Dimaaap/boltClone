const helpPopup = document.getElementById("help-popup");
const openHelpPopupButton = document.getElementById("open-popup");
const closePopupButton = document.getElementById("close-popup");

let isPopupOpen = false;


openHelpPopupButton.addEventListener("click", () => {
    helpPopup.style.display = "block";
    setTimeout(() => {
        helpPopup.classList.add("show");
    }, 1)
    document.body.style.overflow = "hidden";
    openHelpPopupButton.style.display = "none";
    closePopupButton.style.display = "inline-block";
})

closePopupButton.addEventListener("click", () => {
    helpPopup.style.display = "none";
    document.body.style.overflow = "auto";
    openHelpPopupButton.style.display = "inline-block";
    closePopupButton.style.display = "none";
})
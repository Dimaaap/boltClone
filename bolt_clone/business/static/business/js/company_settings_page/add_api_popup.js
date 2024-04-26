const allowApiBtn = document.getElementById("allow-api");
const apiOverlay = document.getElementById("api-overlay");
const apiPopup = document.getElementById("api-popup");
const closeApiPopup = document.getElementById("close-popup-btn-api")
const noBtn = document.getElementById("no-btn");
const yesBtn = document.getElementById("yes-btn");

let isApiPopupOpen = false;

allowApiBtn.addEventListener("click", () => {
    if(!isApiPopupOpen){
        apiOverlay.style.display = "block";
        apiPopup.style.display = "block";
    } else {
        apiOverlay.style.display = "none";
        apiPopup.style.display = "none";
    }
    isApiPopupOpen = !isApiPopupOpen;
})

closeApiPopup.addEventListener("click", () => {
    apiOverlay.style.display = "none";
    apiPopup.style.display = "none";
    isApiPopupOpen = false;
})

noBtn.addEventListener("click", () => {
    apiOverlay.style.display = "none";
    apiPopup.style.display = "none";
    isApiPopupOpen = false;
})
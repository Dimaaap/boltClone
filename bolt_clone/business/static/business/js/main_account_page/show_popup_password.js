const openPopupBtn = document.getElementById("change-password-btn");
const overlay = document.querySelector(".overlay");
const popup = document.querySelector(".popup");
const cancelBtn = document.querySelector(".cancel-btn");

document.addEventListener("DOMContentLoaded", () => {

    overlay.addEventListener("click", () => {
        overlay.style.display = "none";
        popup.style.display = "none";
    })

    openPopupBtn.addEventListener("click", (event) => {
        event.preventDefault();
        overlay.style.display = "block";
        popup.style.display = "block";
    })

    cancelBtn.addEventListener("click", () => {
        overlay.style.display = "none";
        popup.style.display = "none"
    })
})
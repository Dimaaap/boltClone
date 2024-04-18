const openPopupBtn = document.getElementById("change-password-btn");
const overlay = document.querySelector(".overlay");
const popup = document.querySelector(".popup");
const cancelBtn = document.querySelector(".cancel-btn");
const form = document.getElementById("change-password-form");
const saveDataBtn = document.querySelector(".save-btn")

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

    form.addEventListener("submit", (event) => {
        event.preventDefault();
        fetch(form.action, {
            method: form.method,
            body: new FormData(form)
        })
        .then(response => {
            if(!response.ok){
                throw new Error("Помилка HTTP", response.status)
            }
            return response.json()
        })
        .then(data => {
            if(data.success) {
                popup.style.display = "none";
                overlay.style.display = "none";
                const ownerId = data.owner_id;
                window.location.href = `127.0.0.1:8000/business/company/${ownerId}/account`;
            } else {
                const errorContainer = document.querySelector(".errorlist")
                errorContainer.innerHTML = data.form_error;
            }
        })
        .catch(error => {
            console.error("Виникла помилка")
        })
    })
})

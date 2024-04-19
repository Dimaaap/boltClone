const openPopupBtn = document.getElementById("change-password-btn");
const overlay = document.querySelector(".overlay");
const popup = document.querySelector(".popup");
const cancelBtn = document.querySelector(".cancel-btn");
const form = document.getElementById("change-password-form");
const saveDataBtn = document.querySelector(".save-btn");
const closePopupBtn = document.querySelector(".close-popup");
const loadingSpinner = document.querySelector(".fa-spinner");


const closePopup = () => {
    overlay.style.display = "none";
    popup.style.display = "none";
}

const openPopup = () => {
    overlay.style.display = "block";
    popup.style.display = "block";
}

document.addEventListener("DOMContentLoaded", () => {

    overlay.addEventListener("click", () => {
        closePopup();
    })

    closePopupBtn.addEventListener("click", () => {
        closePopup();
        clearErrorMessages();
    })

    openPopupBtn.addEventListener("click", (event) => {
        event.preventDefault();
        openPopup();
        clearErrorMessages();
    })

    cancelBtn.addEventListener("click", () => {
        closePopup();
        clearErrorMessages()
    })

    form.addEventListener("submit", (event) => {
        event.preventDefault();
        clearErrorMessages();
        loadingSpinner.style.display = "inline-block";
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
            loadingSpinner.style.display = "none"
            saveDataBtn.innerHTML = "Зберегти"
            if(data.success) {
                popup.style.display = "none";
                overlay.style.display = "none";
                const ownerId = data.owner_id;
                window.location.href = `/business/company/${ownerId}/account`;
            } else {
                if(data.field === 1){
                    const errorContainer = document.querySelector(".errorlist")
                    errorContainer.innerHTML = data.form_error;
                } else {
                    const errorContainer = Array.from(document.querySelectorAll(".errorlist"))[1]
                    errorContainer.innerHTML = data.form_error;
                }
                console.log(data.form_error)
            }
        })
        .catch(error => {
            loadingSpinner.style.display = "none";
            saveDataBtn.innerHTML = "Зберегти"
            console.error("Виникла помилка", error)
        })
    })

    const clearErrorMessages = () => {
        const errorContainer = document.querySelectorAll(".errorlist")
        errorContainer.forEach(container => {
            container.innerHTML = "";
        })
    }
})


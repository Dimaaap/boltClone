const addEmailBtn = document.getElementById("add-email-btn");
const emailOverlay = document.getElementById("email-overlay");
const emailPopup = document.getElementById("email-popup");
const closeEmailPopup = document.getElementById("close-popup-btn");
const emailForm = document.getElementById("add-pdf-email-form");
const emailFormInput = emailForm.querySelectorAll("input")[1];
const cancelIcon = document.getElementById("email-form-cancel-icon");
const emailSubmit = document.getElementById("email-form-submit");


let isEmailPopupOpen = false;

addEmailBtn.addEventListener("click", () => {
    if(!isEmailPopupOpen){
        emailOverlay.style.display = "block";
        emailPopup.style.display = "block";
    } else {
        emailOverlay.style.display = "none";
        emailPopup.style.display = "none";
    }
    isEmailPopupOpen = !isEmailPopupOpen;
})

closeEmailPopup.addEventListener("click", () => {
    console.log("click");
    emailOverlay.style.display = "none";
    emailPopup.style.display = "none";
    isEmailPopupOpen = false;
})

cancelIcon.addEventListener("click", () => {
    emailFormInput.value = "";
    cancelIcon.style.display = "none";
    emailSubmit.disabled = true;
    emailSubmit.classList.remove("active");
})

emailFormInput.addEventListener("input", () => {
    if(emailFormInput.value.length >= 1){
        cancelIcon.style.display = "block";
        emailSubmit.removeAttribute("disabled");
        emailSubmit.classList.add("active");
    }
})


emailForm.addEventListener("submit", event => {
    event.preventDefault();
    fetch(emailForm.action, {
        method: emailForm.method,
        body: new FormData(emailForm)
    })
    .then(response => {
        if(!response.ok){
            throw new Error("Помилка HTTP", response.status)
        }
        return response.json()
    })
    .then(data => {
        if(data.success) {
            const ownerId = data.owner_id;
            window.location.href = `/business/company/${ownerId}/settings`;
        } else {
            const errorContainer = document.querySelector(".errorlist")
            errorContainer.innerHTML = data.form_error;
        }
    })
    .catch(error => {
        console.error("Виникла помилка", error)
    })
})
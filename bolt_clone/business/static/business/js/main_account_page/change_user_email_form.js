const openChangeEmailFormBtn = document.getElementById("change-user-email");
const changeEmailContainer = document.querySelectorAll(".hidden-form")[1];
const userEmail = document.getElementById("user-email");
const fieldLabelsIcons = document.querySelector(".user-email-icon");
const field = document.querySelector("#change-email-form .form-control");
const emailForm = document.getElementById("change-email-form");


const oldUserEmail = userEmail.innerHTML


let isSectionOpen = false;


openChangeEmailFormBtn.addEventListener("click", () => {
    if(!isSectionOpen){
        changeEmailContainer.style.display = "block";
        openChangeEmailFormBtn.innerHTML = "Скасувати"
        userEmail.innerHTML = "Оновіть адресу робочої електронної пошти"
    } else {
        changeEmailContainer.style.display = "none";
        openChangeEmailFormBtn.innerHTML = "Змінити"
        userEmail.innerHTML = oldUserEmail;
    }
    isSectionOpen = !isSectionOpen;
})

field.addEventListener("mouseover", () => {
    fieldLabelsIcons.style.display = "inline-block";
    fieldLabelsIcons.addEventListener("mouseover", () => {
        fieldLabelsIcons.style.display = "inline-block";
    })
})

field.addEventListener("mouseout", () => {
    fieldLabelsIcons.style.display = "none";
})

fieldLabelsIcons.addEventListener("click", () => {
    field.value = "";
})

emailForm.addEventListener("submit", (event) => {
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
        if(data.success){
            const ownerId = data.owner_id;
            window.location.href = `/business/company/${ownerId}/account`;
        } else {
            const errors = document.querySelector(".error-user-email");
            errors.innerHTML = data.form_error;
        }
    })
    .catch(error => {
        console.error("Виникла помилка", error)
    })
})
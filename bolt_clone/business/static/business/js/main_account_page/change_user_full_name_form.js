const openChangeNameFormBtn = document.getElementById("change-user-full-name");
const changeNameContainer = document.querySelector(".hidden-form");
const userName = document.getElementById("user-name");
const fieldLabels = Array.from(document.querySelectorAll(".input-field-icon"));
const fields = Array.from(document.querySelectorAll(".hidden-form .form-control"));
const usernameForm = document.getElementById("change-name-form");

const oldUserNameHTML = userName.innerHTML

let isContainerOpen = false;


openChangeNameFormBtn.addEventListener("click", () => {
    if(!isContainerOpen){
        changeNameContainer.style.display = "block";
        openChangeNameFormBtn.innerHTML = "Скасувати"
        userName.innerHTML = "Оновіть своє ім'я"
    } else {
        changeNameContainer.style.display = "none";
        openChangeNameFormBtn.innerHTML = "Змінити"
        userName.innerHTML = oldUserNameHTML;
    }
    isContainerOpen = !isContainerOpen
})


fields.forEach((field) => {
    let fieldIndex = fields.indexOf(field)
    field.addEventListener("mouseover", () => {
        fieldLabels[fieldIndex].style.display = "inline-block";
        fieldLabels[fieldIndex].addEventListener("mouseover", () => {
            fieldLabels[fieldIndex].style.display = "inline-block";
        })
    })
    field.addEventListener("mouseout", () => {
        fieldLabels[fieldIndex].style.display = "none";
    })
})

fieldLabels.forEach(label => {
    let labelIndex = fieldLabels.indexOf(label);
    label.addEventListener("click", () => {
        fields[labelIndex].value = "";
    })
})

usernameForm.addEventListener("submit", (event) => {
    event.preventDefault();
    fetch(usernameForm.action, {
        method: usernameForm.method,
        body: new FormData(usernameForm)
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
            window.location.href = `/business/company/${ownerId}/account`;
        } else {
            const errorContainer = document.querySelector(".error-user-name")
            errorContainer.innerHTML = data.form_error;
        }
    })
    .catch(error => {
        console.error("Виникла помилка", error)
    })
})
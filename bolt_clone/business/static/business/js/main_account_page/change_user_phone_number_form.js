const openChanePhoneNumberFormBtn = document.getElementById("change-phone-number-btn");
const changePhoneNumberContainer = document.querySelectorAll(".hidden-form")[2]
const userPhoneNumber = document.getElementById("user-phone-number");
const fieldLabelsIcon = document.querySelector(".user-phone-icon");
const userPhoneNumberField = document.querySelector("#change-phone-number-form .form-control");
const phoneNumberForm = document.getElementById("change-phone-number-form")
console.log(phoneNumberForm)

const oldUserPhone = userPhoneNumber.innerHTML;


let isFormOpen = false;


openChanePhoneNumberFormBtn.addEventListener("click", () => {
    if(!isFormOpen) {
        changePhoneNumberContainer.style.display = "block";
        openChanePhoneNumberFormBtn.innerHTML = "Скасувати";
        userPhoneNumber.innerHTML = "Оновіть ваш номер телефону";
    } else {
        changePhoneNumberContainer.style.display = "none";
        openChanePhoneNumberFormBtn.innerHTML = "Змінити";
        userPhoneNumber.innerHTML = oldUserPhone;
    }
    isFormOpen = !isFormOpen;
})

phoneNumberForm.addEventListener("submit", (event) => {
    event.preventDefault();
    fetch(phoneNumberForm.action, {
        method: phoneNumberForm.method,
        body: new FormData(phoneNumberForm)
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
            const errors = document.querySelector(".error-user-phone")
            errors.innerHTML = data.form_error;
        }
    })
    .catch(error => {
        console.error("Виникла помилка", error)
    })
})
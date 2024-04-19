const openChangeNameFormBtn = document.getElementById("change-user-full-name");
const changeNameContainer = document.querySelector(".hidden-form");
const userName = document.getElementById("user-name");

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
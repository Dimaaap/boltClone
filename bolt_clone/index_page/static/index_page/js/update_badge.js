const selectOptions = document.querySelectorAll(".category-container");
const selectLabels = document.querySelectorAll(".category-container label");
const selectInputs = document.querySelectorAll(".category-container input");
const badge = document.getElementById("cuisine_badge");
const badgeContainer = document.getElementById("badge-container");
const errorMessageContainer = document.getElementById("error-message-container");

let selectedOptions = 0;


const createNewBadge = (checkboxId, badgeId) => {
    let newBadge = document.createElement("div");
    newBadge.setAttribute("id", badgeId);
    newBadge.setAttribute("class", "category-badge");
    newBadge.innerHTML = selectLabels[checkboxId].innerHTML;
    return newBadge
}

const createCloseBadgeButton = () => {
    let closeButton = document.createElement("button");
    closeButton.innerHTML = "x";
    return closeButton;
}

const addNewBadge = (checkbox, closeBtn, newBadge) => {
    closeBtn.addEventListener("click", () => {
        newBadge.remove();
        selectedOptions --;
        checkbox.checked = false;
        let existingErrorMessage = errorMessageContainer.querySelector(".error-message");
        if(existingErrorMessage){
            existingErrorMessage.remove();
        }
    })
    appendBtnToBadge(newBadge, closeBtn)
}


const appendBtnToBadge = (newBadge, btn) => {
    newBadge.appendChild(btn);
    badgeContainer.appendChild(newBadge);
    selectedOptions ++;
}


const checkboxNotChecked = (existingBadge, checkbox) => {
    if(existingBadge) {
        existingBadge.remove()
    }
    selectedOptions --;
    checkbox.checked = false;
}

const generateErrorMessage = () => {
    let existingErrorMessageContainer = errorMessageContainer.querySelector(".error-message");
    if(existingErrorMessageContainer){
        existingErrorMessageContainer.innerHTML = "Максимум можна вибрати 4 категорії"
    } else {
        displayErrorMessage()
    }
}

const displayErrorMessage = () => {
    let textMessage = document.createElement("p");
    textMessage.innerHTML = "Максимум можна вибрати 4 категорії";
    textMessage.className = "error-message";
    errorMessageContainer.appendChild(textMessage)
}

const removeErrorMessage = () => {
   let existingErrorMessage = errorMessageContainer.querySelector(".error-message");
   if(existingErrorMessage) {
      existingErrorMessage.remove();
   }
}


selectInputs.forEach((checkbox) => {
    checkbox.addEventListener("change", () => {
        let checkboxId = Array.from(selectInputs).indexOf(checkbox);
        let badgeId = "badge_" + checkboxId;
        let existingBadge = document.getElementById(badgeId);
        if(checkbox.checked && selectedOptions < 4){
            if(existingBadge){
                existingBadge.remove();
            }
            const newBadge = createNewBadge(checkboxId, badgeId);
            const closeButton = createCloseBadgeButton();
            addNewBadge(checkbox, closeButton, newBadge);
        } else if (!checkbox.checked){
            checkboxNotChecked(existingBadge, checkbox)
        } else if (checkbox.checked && selectedOptions >= 4){
            generateErrorMessage();
            checkbox.checked = false;
        }
        else {
            removeErrorMessage();
        }
    })
})
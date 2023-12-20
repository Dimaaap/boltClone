const selectOptions = document.querySelectorAll(".category-container");
const selectLabels = document.querySelectorAll(".category-container label");
const selectInputs = document.querySelectorAll(".category-container input");
const badge = document.getElementById("cuisine_badge");
const badgeContainer = document.getElementById("badge-container");

let selectedOptions = 0;


selectInputs.forEach((checkbox) => {
    checkbox.addEventListener("change", () => {
        let checkboxId = Array.from(selectInputs).indexOf(checkbox);
        let badgeId = "badge_" + checkboxId;
        let existingBadge = document.getElementById(badgeId);
        if(checkbox.checked && selectedOptions < 4){
            if(existingBadge){
                existingBadge.remove();
            }
            let newBadge = document.createElement("div");
            newBadge.setAttribute("id", "badge");
            newBadge.innerHTML = selectLabels[checkboxId].innerHTML;
            badgeContainer.appendChild(newBadge);
            selectedOptions++;
        } else if (!checkbox.checked){
            if(existingBadge){
                existingBadge.remove();
            }
            selectedOptions--;
        } else {
            let textMessage = document.createElement("p");
            textMessage.innerHTML = "Максимум можна вибрати до 4 категорій"
            textMessage.className = "error-message";
            badgeContainer.appendChild(textMessage);
            checkbox.checked = false;
        }
    })
})
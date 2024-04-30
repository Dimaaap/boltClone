const allowPromoBtn = document.getElementById("allow-promo");
const promoOverlay = document.getElementById("promo-overlay");
const promoPopup = document.getElementById("promo-popup");
const closePromoPopup = document.getElementById("close-popup-btn-promo");
const addPromoForm = document.getElementById("add-promo-code-form");
const promoLabel = addPromoForm.querySelector("label");
const promoInput = addPromoForm.querySelector(".form-control");


let isPromoPopupOpen = false;

const openPopup = () => {
    promoOverlay.style.display = "block";
    promoPopup.style.display = "block";
}


const closePopup = () => {
    promoOverlay.style.display = "none";
    promoPopup.style.display = "none";
}

allowPromoBtn.addEventListener("click", () => {
    if(!isPromoPopupOpen){
        openPopup()
    } else {
        closePopup()
    }
    ifPromoPopupOpen = !isPromoPopupOpen;
})

closePromoPopup.addEventListener("click", () => {
    closePopup();
    isPromoPopupOpen = false;
})


promoInput.addEventListener("click", () => {
    promoLabel.style.display = "inline-block";
    promoInput.placeholder = "Введіть промокод";
})

promoInput.addEventListener("blur", () => {
    promoLabel.style.display = "none";
    promoInput.placeholder = "Промокод";
})

addPromoForm.addEventListener("submit", event => {
    event.preventDefault();
    fetch(addPromoForm.action, {
        method: addPromoForm.method,
        body: new FormData(addPromoForm)
    })
    .then(response => {
        console.log(response)
        if(!response.ok){
            throw new Error("Помилка HTTP", response.status)
        }
        return response.json()
    })
    .then(data => {
        if(data.success){
            const ownerId = data.owner_id;
            window.location.href = `/business/company/${ownerId}/settings`;
        } else {
            const errorContainer = addPromoForm.querySelector(".errorlist")
            errorContainer.innerHTML = data.form_error;
        }
    })
    .catch(error => {
        console.error("Виникла помилка", error);
    })
})
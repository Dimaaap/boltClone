const deliveryModalTrigger = document.getElementById("delivery-trigger");
const deliveryModal = document.getElementById("delivery-modal");
const openInnerBtn = document.getElementById("open-inner-content");
const dropdownContent = document.querySelector(".dropdown-content");
const innerContent = document.querySelector(".inner-content");
const hideInner = document.getElementById("hide-inner");
const incomeModal = document.getElementById("income-modal");

let isModalOpen = false;

openInnerBtn.addEventListener("click", () => {
    dropdownContent.style.display = "none";
    innerContent.style.display = "block";
})

hideInner.addEventListener("click", () => {
    dropdownContent.style.display = "block";
    innerContent.style.display = "none";
})

deliveryModalTrigger.addEventListener("mouseenter", () => {
    deliveryModal.style.display = "block";
    incomeModal.style.display = "none";
    isModalOpen = !isModalOpen;
})

deliveryModalTrigger.addEventListener("click", () => {
    if(!isModalOpen) {
        deliveryModal.style.display = "block";
    } else {
        deliveryModal.style.display = "none";
    }
    isModalOpen = !isModalOpen;
})

deliveryModal.addEventListener("mouseleave", () => {
    deliveryModal.style.display = "none";
    isModalOpen = !isModalOpen;
})
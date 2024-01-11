const openIncome = document.getElementById("open-income");
const modalIncome = document.getElementById("income-modal");
const modalDelivery = document.getElementById("delivery-modal");
const openInnerIncome = document.getElementById("open-inner-content-second-icon");
const innerIncomeContent = document.getElementById("income-inner");
const mainContent = document.getElementById("main-content");
const secondInner = document.getElementById("second-inner");


let isOpen = false;

openInnerIncome.addEventListener("click", () => {
    mainContent.style.display = "none";
    innerIncomeContent.style.display = "block";
})

secondInner.addEventListener("click", () => {
    mainContent.style.display = "block";
    innerIncomeContent.style.display = "none";
})

openIncome.addEventListener("mouseenter", () => {
    modalIncome.style.display = "block";
    modalDelivery.style.display = "none";
    isOpen = true;
})

modalIncome.addEventListener("mouseleave", () => {
    modalIncome.style.display = "none";
    isOpen = false;
})

openIncome.addEventListener("click", () => {
    if(!isOpen) {
        modalIncome.style.display = "block";
    } else {
        modalIncome.style.display = "none"
    }
    isOpen = !isModalOpen
})

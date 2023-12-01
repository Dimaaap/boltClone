const selectInput = document.querySelector(".main-content form select");
const icon = document.querySelector(".main-content form i");

let isIconRotated = false;

selectInput.addEventListener("click", () => {
    isIconRotated = !isIconRotated;
    icon.style.transform = isIconRotated ? "rotate(180deg)" : "";
    icon.style.transformOrigin = isIconRotated ? "50% 20%" : "";
})
const clearFieldValueBtn = document.getElementById("clear-field-value");
const citySelect = document.getElementById("city-select-field");
const dropdownSelect = Array.from(document.querySelectorAll(".dropdown .cities-ul li"));

clearFieldValueBtn.addEventListener("click", () => {
    citySelect.value = ""
})

dropdownSelect.forEach((li) => {
    li.addEventListener("click", () => {
        citySelect.value = li.innerText;
    })
})
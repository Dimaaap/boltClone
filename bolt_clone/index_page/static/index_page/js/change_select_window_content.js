let countrySelect = document.querySelector('.select-country-flag');

document.addEventListener("DOMContentLoaded", () => {
    countrySelect.addEventListener("change", () => {
        let selectedOption = countrySelect.options[countrySelect.selectedIndex];
        let optionContent = String(selectedOption.textContent);
        let countryEmoji = optionContent.slice(0, 3);
        let countryCode = optionContent.slice(optionContent.indexOf("(") + 1, optionContent.indexOf(")"));
        let newFieldValue = `${countryEmoji} ${countryCode}`

    })
})
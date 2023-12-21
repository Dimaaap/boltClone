const nicheField = document.getElementById("id_partner_niche");
const cuisineField = document.querySelector(".conditional-field");


nicheField.addEventListener("change", () => {
    if(nicheField.value !== "Заклад харчування") {
        cuisineField.style.display = 'none';
    } else {
        cuisineField.style.display = 'block';
    }
})
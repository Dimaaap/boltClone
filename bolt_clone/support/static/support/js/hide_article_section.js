const categoriesSection = document.getElementById("categories-section");
const searchForm = document.getElementById("search-form");

searchForm.addEventListener("input", (event) => {
    let inputValue = event.target.value.trim();

    if(inputValue.length >= 1){
        categoriesSection.style.display = "none";
    } else {
        categoriesSection.style.display = "block";
    }
})
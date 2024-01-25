const searchResultSection = document.getElementById("search-results");
const categoriesSection = document.getElementById("categories-section");
const searchForm = document.getElementById("search-form");


searchForm.addEventListener("input", (event) => {
    let inputValue = event.target.value.trim();
    console.log(searchResultSection)

    if(inputValue.length >= 1){
        searchResultSection.style.display = "block";
        categoriesSection.style.display = "none";
    } else {
        searchResultSection.style.display = "none";
        categoriesSection.style.display = "block";
    }
})
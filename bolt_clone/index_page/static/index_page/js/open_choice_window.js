const cuisineChoiceField = document.getElementById("cuisine-choice");
const modalWindow = document.querySelector("#modal-cuisine-choice .modal-content");
let badgesContainer = document.getElementById("badge-container");
const badges = document.getElementById("cuisine_badge");



let modalOpen = false;

cuisineChoiceField.addEventListener("click", () => {
    if(!modalOpen){
        modalWindow.style.display = "block";
        modalWindow.classList.add("active");
    } else {
        modalWindow.style.display = "none";
        modalWindow.classList.remove("active");
    }
    modalOpen = !modalOpen;
})


document.addEventListener("click", (event) => {
    if(!modalWindow.contains(event.target) && event.target !== cuisineChoiceField && event.target !== badgesContainer) {
        console.log("click click")
        modalWindow.style.display = "none";
        modalWindow.classList.remove("active");
        modalOpen = !modalOpen;
    }
})
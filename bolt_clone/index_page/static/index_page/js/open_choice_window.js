const cuisineChoiceField = document.getElementById("cuisine-choice");
const modalWindow = document.querySelector("#modal-cuisine-choice .modal-content");
let badgesContainer = document.getElementById("badge-container");
const badges = document.getElementById("cuisine_badge");

console.log(badges);



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

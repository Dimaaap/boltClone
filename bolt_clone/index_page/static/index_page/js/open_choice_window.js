const cuisineChoiceField = document.getElementById("cuisine-choice");
const modalWindow = document.querySelector("#modal-cuisine-choice .modal-content");

let modalOpen = false;


cuisineChoiceField.addEventListener("click", () => {
    if(!modalOpen){
        modalWindow.style.display = "block";
    } else {
        modalWindow.style.display = "none";
    }
    modalOpen = !modalOpen;
})
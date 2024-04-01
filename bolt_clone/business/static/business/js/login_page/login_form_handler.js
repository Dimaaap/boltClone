const emailBtn = document.getElementById("send-email");
const hiddenField = document.querySelector(".hidden-group");
const passwordField = document.getElementById("owner_password");
const submitBtn = document.getElementById("submit-btn");
const emailField = document.getElementById("owner_email");


console.log("asdasdas");


emailBtn.addEventListener("click", (event) => {
    if(owner_email.value.length >= 1){
        event.preventDefault();
        hiddenField.classList.remove("hidden-group")
        emailBtn.innerText = "Увійти"
        passwordField.required = true;
        emailBtn.style.visibility = "hidden";
        submitBtn.style.visibility = "visible";
    }
})
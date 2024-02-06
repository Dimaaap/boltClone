const firstChangeBtn = document.getElementById("first-btn");
const secondChangeBtn = document.getElementById("second-btn");
const firstForm = document.getElementById("report-form");
const secondForm = document.getElementById("other-report-form");

secondForm.style.display = "none";

firstChangeBtn.addEventListener("click", () => {
    if(!firstChangeBtn.classList.contains("active")){
        firstChangeBtn.classList.add("active");
        secondChangeBtn.classList.remove("active");
        secondForm.style.display = "none";
        firstForm.style.display = "block";
    }
})

secondChangeBtn.addEventListener("click", () => {
    if(!secondChangeBtn.classList.contains("active")){
        secondChangeBtn.classList.add("active");
        firstChangeBtn.classList.remove("active");
        secondForm.style.display = "block";
        firstForm.style.display = "none";
    }
})
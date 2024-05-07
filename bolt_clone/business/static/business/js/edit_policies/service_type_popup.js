const serviceTypePopup = document.getElementById("service-kind");
const serviceTypeCheckbox = document.getElementById("kind_service");


let isServiceTimeOpen = false;


serviceTypeCheckbox.addEventListener("change", () => {
    if(!isServiceTimeOpen) {
        serviceTypePopup.style.display = "block";
    } else {
        serviceTypePopup.style.display = "none";
    }

    isServiceTimeOpen = !isServiceTimeOpen;
})


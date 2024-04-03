const countriesInput = document.getElementById("company_country");
const countriesDropdown = document.getElementById("countries-select-modal");
const btn = document.getElementById("first");
const countriesP = Array.from(countriesDropdown.querySelectorAll("p"));
const secondBtn = document.getElementById("second");
const employeesModal = document.getElementById("workers-count-modal");
const employeesCountField = document.getElementById("workers_count");
const employeesP = Array.from(employeesModal.querySelectorAll("p"));


let isModalOpen = false;
let isEmployeesModalOpen = false;

const openCloseModal = () => {
    if(isModalOpen){
        countriesDropdown.style.display = "none";
        btn.style.top = "85%";
        secondBtn.style.top = "98.5%"
    } else {
        countriesDropdown.style.display = "block";
        btn.style.top = "138%";
        secondBtn.style.top = "152%";
        isEmployeesModalOpen = false;
    }
    isModalOpen = !isModalOpen;
}

const openCloseEmployeesModal = () => {
    if(isEmployeesModalOpen){
        employeesModal.style.display = "none";
        secondBtn.style.top = "98.5%";
    } else {
        employeesModal.style.display = "block";
        countriesDropdown.style.display = "none";
        secondBtn.style.top = "130%";
        isModalOpen = false;
    }
    isEmployeesModalOpen = !isEmployeesModalOpen;
}

btn.addEventListener("click", () => {
    openCloseModal();
})

secondBtn.addEventListener("click", () => {
    openCloseEmployeesModal();
})

countriesP.forEach((country) => {
    country.addEventListener("click", () => {
        countriesInput.value = country.innerText;
        openCloseModal();
    })
})


employeesP.forEach((employee) => {
    employee.addEventListener("click", () => {
        employeesCountField.value = employee.innerText;
        openCloseEmployeesModal();
    })
})
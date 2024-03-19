const sendInputDateBtnArray = Array.from(document.querySelectorAll(".agree-btn"));
const dropdownArray = Array.from(document.querySelectorAll(".dropdown_modal"));
const dateInputFieldArray = Array.from(document.querySelectorAll(".date-input"));
const errorContainerArray = Array.from(document.querySelectorAll(".input-errors"));
const uploadFileFieldArray = Array.from(document.querySelectorAll("input[type='file']"));
const documentContainerArray = Array.from(document.querySelectorAll(".document-container"));


let todayDay = new Date();


const sendAJAXRequest = (file, expTime, fieldName) => {
    let formData = new FormData();
    formData.append("exp_time", expTime);
    formData.append("field_name", fieldName);
    formData.append("file", file)

    const URLAddress = `/driver/save_file/${fieldName}/${expTime}/`;

    fetch(URLAddress, {
        method: "POST",
        body: formData,
        headers: {
            "X-CSRFToken": getCookie("csrftoken")
        },
    })
    .then(response => {
        if(!response.ok) {
            throw new Error(`HTTP Error! status: ${response.status}`);
        } else if (response.headers.get("Content-Type").includes("application/json")){
            return response.json();
        } else {
            throw new Error("Not JSON response")
        }
    })
    .then(data => {
        console.log(data)
    })
    .catch(error => console.error("Error: ", error))
}

const getCookie = (name) => {
    const cookieValue = document.cookie
        .split("; ")
        .find(row => row.startsWith(`${name}=`))
        ?.split("=")[1];
    return cookieValue ? decodeURIComponent(cookieValue) : null;
}

sendInputDateBtnArray.forEach(btn => {
    let btnIndex = sendInputDateBtnArray.indexOf(btn);
    let dateInput = dateInputFieldArray[btnIndex];
    let errorContainer = errorContainerArray[btnIndex];
    let fileInput = uploadFileFieldArray[btnIndex];

    btn.addEventListener("click", e => {
        e.preventDefault();
        let btnIndex = sendInputDateBtnArray.indexOf(btn);
        let documentContainer = documentContainerArray[btnIndex];
        let dateValue = dateInput.value;
        let fileInputName = fileInput.name;

        let uploadedFile = documentContainer.querySelector("img")
        let file = uploadedFile.src

        if(dateValue) {
            const inputDate = Date.parse(dateValue);
            if(inputDate <= todayDay) {
                errorContainer.innerText = "Неприпустима дата строку дії. Переконайтесь, що обрана дата в майбутньому"
            } else {
                sendAJAXRequest(file, dateValue, fileInputName);
                dropdownArray[btnIndex].style.display = "none";
                location.reload();
            }
        } else {
            errorContainer.innerText = "Поле обов'язкове для заповнення"
        }
    })
})
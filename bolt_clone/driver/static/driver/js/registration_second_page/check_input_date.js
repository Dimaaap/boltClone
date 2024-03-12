const sendInputDateBtnArray = Array.from(document.querySelectorAll(".agree-btn"));
const dropdownArray = Array.from(document.querySelectorAll(".dropdown_modal"));
const dateInputFieldArray = Array.from(document.querySelectorAll(".date-input"));
const errorContainerArray = Array.from(document.querySelectorAll(".input-errors"));
const uploadFileFieldArray = Array.from(document.querySelectorAll("input[type='file']"));


let todayDay = new Date();


const sendAJAXRequest = (file, expTime, fieldName) => {
    let formData = new FormData();
    formData.append("file", file);
    formData.append("exp_time", expTime);
    formData.append("field_name", fieldName);

    const URLAddress = `127.0.0.1/driver/save_file/${fieldName}/${expTime}/`;

    fetch(URLAddress, {
        method: "POST",
        body: formData,
        headers: {
            "X-CSRFToken": getCookie("csrftoken")
        },
    })
    .then(response => response.json())
    .catch(error => console.error('Error: ', error))
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
        let dateValue = dateInput.value;
        let fileInputName = fileInput.name;
        let file = fileInput.value;

        if(dateValue) {
            const inputDate = Date.parse(dateValue);
            if(inputDate <= todayDay) {
                errorContainer.innerText = "Неприпустима дата строку дії. Переконайтесь, що обрана дата в майбутньому"
            } else {
                console.log("Sending AJAX request...")
                sendAJAXRequest(file, dateValue, fileInputName);
            }
        } else {
            errorContainer.innerText = "Поле обов'язкове для заповнення"
        }
    })
})
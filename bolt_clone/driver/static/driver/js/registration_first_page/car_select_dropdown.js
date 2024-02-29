const carSelectDropdown = document.getElementById("car-model-select");
const carSelectDropdownField = document.getElementById("driver-car-select");
const carSelectChevron = document.querySelector(".fa-angle-down");


let isModalOpen = false;


const showHideDropdown = () => {
    if(!isModalOpen){
        carSelectDropdown.style.display = "block";
    } else {
        carSelectDropdown.style.display = "none";
    }
    isModalOpen = !isModalOpen;
}

const fetchData = (inputValue, csrfToken, deviceIp) => {
    fetch(`/driver/search/${deviceIp}`, {
        method: "POST",
        body: JSON.stringify({"term": inputValue}),
        headers: {
            "Content-Type": "application/json",
            "X-CSRFToken": csrfToken
        }
    })
    .then(response => response.json())
    .then(data => {
        let resultHtml = ''
        if(data.length < 1){
            resultHtml = `<p class=no-options-text>No options</p>`;
        }
        data.forEach((car) => {
            resultHtml += `<div class=car-section>
                                    <p class=found-cars>${car.model_title}</p>
                                </div>`
        });
        carSelectDropdown.innerHTML = resultHtml;
    })
}

carSelectDropdownField.addEventListener("click", () => {
    showHideDropdown()
})

carSelectChevron.addEventListener("click", () => {
    showHideDropdown()
})


carSelectDropdownField.addEventListener("keyup", () => {
    let inputValue = carSelectDropdownField.value.trim();
    let csrfToken = getCookie("csrftoken");
    let deviceIp = "127.0.0.1";
    carSelectDropdown.display = "block";
    isModalOpen = true;

    if(inputValue.length > 0){
        carSelectDropdown.style.top = "100%";
        fetchData(inputValue, csrfToken, deviceIp)
    } else {
        carSelectDropdown.style.top = "55%";
        fetchData(inputValue, csrfToken, deviceIp)
    }
})

function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
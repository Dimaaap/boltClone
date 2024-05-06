let salesLimitPopup = document.getElementById("limit-select")
let salesLimitCheckbox = document.getElementById("cost_level_track")

let isSalesLimitOpen = false;


salesLimitCheckbox.addEventListener("change", () => {
    if(!isSalesLimitOpen){
        salesLimitPopup.style.display = "block";
    } else {
        salesLimitPopup.style.display = "none"
    }
    isSalesLimitOpen = !isSalesLimitOpen;
})
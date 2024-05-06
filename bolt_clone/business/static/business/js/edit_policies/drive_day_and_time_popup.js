const driveTimePopup = document.getElementById("trips-by-days");
const driveTimeCheckbox = document.getElementById("drive_day_and_time");

let isDriveTimeOpen = false;


driveTimeCheckbox.addEventListener("change", () => {
    if(!isDriveTimeOpen){
        driveTimePopup.style.display = "block"
    } else {
        driveTimePopup.style.display = "none";
    }
    isDriveTimeOpen = !isDriveTimeOpen;
})
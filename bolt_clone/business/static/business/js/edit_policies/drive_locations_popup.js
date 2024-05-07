const driveLocationsPopup = document.getElementById("drive-locations");
const driveLocationsCheckbox = document.getElementById("drive_places");


let isDriveLocationsOpen = false;


driveLocationsCheckbox.addEventListener("change", () => {
    if(!isDriveLocationsOpen){
        driveLocationsPopup.style.display = "block";
    } else {
        driveLocationsPopup.style.display = "none";
    }

    isDriveLocationsOpen = !isDriveLocationsOpen;
})
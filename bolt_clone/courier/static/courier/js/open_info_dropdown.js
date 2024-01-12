const openDropdownBtn = document.getElementById("open-info-dropdown");
const infoDropdown = document.getElementById("info-dropdown");

let infoOpen = false;

const changeButtonStyle = (btn) => {
    btn.style.backgroundColor = "rgba(0, 0, 0, 0.7)"
    btn.style.color = "white";
}

openDropdownBtn.addEventListener("click", () => {
    if(!infoOpen){
        infoDropdown.style.display = "block";
        changeButtonStyle(openDropdownBtn);
    } else {
        infoDropdown.style.display = "none";
        openDropdownBtn.classList.remove("active");
        openDropdownBtn.style.backgroundColor = "transparent";
        openDropdownBtn.style.color = "black";
    }
    infoOpen = !infoOpen;
})
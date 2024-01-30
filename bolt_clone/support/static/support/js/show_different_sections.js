const headerLinks = Array.from(document.querySelectorAll(".popup-section-header .header li"));
const sections = Array.from(document.querySelectorAll(".header-container"));


let currentLinkActive = 0;
let currentSection = 0;


const allSectionsHide = () => {
    for(let section of sections){
        section.style.display = "none";
    }
}

const clearAllActiveSections = () => {
    for (let header of headerLinks){
        headerLink = Array.from(header.childNodes)[0];
        headerLink.classList.remove("active-section")
    }
}

for(const header of headerLinks) {
    header.addEventListener("click", () => {
        currentLinkActive = headerLinks.indexOf(header);
        currentSection = sections[currentLinkActive];
        allSectionsHide();
        clearAllActiveSections();
        headerLink = Array.from(header.childNodes)[0];
        headerLink.classList.add("active-section");
        currentSection.style.display = "block";
    })
}

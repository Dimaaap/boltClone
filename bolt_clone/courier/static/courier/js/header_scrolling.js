const header = document.querySelector("header");
console.log(header);

document.addEventListener("DOMContentLoaded", () => {
    window.addEventListener("scroll", () => {
        if(window.scrollY > 0) {
            header.style.backgroundColor = "black";
            console.log(header.style.backgroundColor);
        } else {
            header.style.backgroundColor = "transparent";
            console.log(header.style.backgroundColor)
        }
    })
})

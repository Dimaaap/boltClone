document.addEventListener("DOMContentLoaded", () => {
    let accordionItem = document.querySelectorAll(".accordion-item");

    accordionItem.forEach((item) => {
        let header = item.querySelector(".accordion-header");

        header.addEventListener("click", () => {
            let content = item.querySelector('.accordion-content');
            let arrow = item.querySelector('.fa-chevron-up');

            if(content.style.display === "none" || content.style.display === ""){
                content.style.display = "block";
                arrow.style.setProperty("--arrow-rotate", "180deg");
            } else {
                content.style.display = "none";
                arrow.style.setProperty("--arrow-rotate", "0deg")
            }
        })
    })
})
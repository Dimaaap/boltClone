const fileInputs = Array.from(document.querySelectorAll("input[type='file']"));
const dropdownContainers = Array.from(document.querySelectorAll(".dropdown_modal"));
const closeButtons = Array.from(document.querySelectorAll(".close"));
const documentContainers = Array.from(document.querySelectorAll(".document-container"));
const photoIsCorrectBtn = Array.from(document.querySelectorAll(".second-btn"));
const carDocumentForm = document.getElementById("car-documents-form");
const documentExpiredForm = document.getElementById("document-data-form");
const hiddenTextContainers = Array.from(document.querySelectorAll(".hidden-text-container"));


const pdfFileHandler = (selectedFile, inputIndex) => {
    const reader = new FileReader();
    reader.onload = e => {
        const data = new Uint8Array(e.target.result);
        pdfjsLib.getDocument(data).promise.then((pdf) => {
            return pdf.getPage(1);
        }).then((page) => {
            const viewport = page.getViewport({scale: 1});
            const canvas = document.createElement("canvas");
            const context = canvas.getContext("2d");
            canvas.height = viewport.height;
            canvas.width = viewport.width;

            const renderContext = {
                canvasContext: context,
                viewport: viewport
            };
            const readerTask = page.render(renderContext);
            readerTask.promise.then(() => {
            const documentContainer = documentContainers[inputIndex];
            documentContainer.innerHTML = `<img class="doc-image"
                    src="${canvas.toDataURL()}" alt="Uploaded Document"/>`;
            })
        })
    }
    reader.readAsArrayBuffer(selectedFile);
}


const imageFileHandler = (selectedFile, inputIndex) => {
    const reader = new FileReader();
    reader.onload = e => {
        const documentContainer = documentContainers[inputIndex];
         documentContainer.innerHTML = `<img class="no-doc-image"
            src="${e.target.result}" alt="Uploaded Document"/>`;
    };
    reader.readAsDataURL(selectedFile);
}


fileInputs.forEach((fileInput) => {
    fileInput.addEventListener("change", (event) => {
        const selectedFile = event.target.files[0];
        let inputIndex = fileInputs.indexOf(fileInput);
        const documentContainer = documentContainers[inputIndex];
        documentContainer.innerHTML = "";

        dropdownContainers[inputIndex].style.display = "block";
        fileInput.value = "";

        if(selectedFile){
            if(selectedFile.type === "application/pdf"){
                pdfFileHandler(selectedFile, inputIndex);
            } else if(selectedFile.type.startsWith("image/")){
                imageFileHandler(selectedFile, inputIndex);
            } else {
                console.error("Unsupported file type");
            }
        }
    });
});

photoIsCorrectBtn.forEach((btn) => {
    btn.addEventListener("click", () => {
        let dropdown = dropdownContainers[photoIsCorrectBtn.indexOf(btn)];
        updateModalContent(dropdown);
    })
})

const updateModalContent = (dropdown) => {
    const textContainer = dropdown.querySelector("#text-container");
    const hiddenText = dropdown.querySelector("#hidden-text-container");
    const hiddenModalTitle = hiddenText.querySelector("h3");
    const hiddenModalDesc = hiddenText.querySelector("p");
    const btnSection = dropdown.querySelector(".btn-section");
    const visibleBtnSection = dropdown.querySelector(".buttons-container")
    const documentDateInput = dropdown.querySelector(".document-date-input");

    textContainer.classList.add("hidden");
    hiddenText.classList.remove("hidden");
    hiddenModalTitle.classList.remove("hidden");
    hiddenModalDesc.classList.remove("hidden");
    btnSection.classList.remove("hidden");
    visibleBtnSection.classList.add("hidden");
    documentDateInput.classList.remove("hidden");
    hiddenText.style.width = "100%";

}

closeButtons.forEach((closeBtn) => {
    closeBtn.addEventListener("click", (event) => {
        event.preventDefault();
        let btnIndex = closeButtons.indexOf(closeBtn);
        let dropdown = dropdownContainers[btnIndex];
        dropdown.style.display = "none";

        const textContainer = dropdown.querySelector("#text-container");
        const hiddenText = dropdown.querySelector("#hidden-text-container");
        const hiddenModalTitle = hiddenText.querySelector("h3");
        const hiddenModalDesc = hiddenText.querySelector("p");
        const btnSection = dropdown.querySelector(".btn-section");
        const visibleBtnSection = dropdown.querySelector(".buttons-container");
        const documentDateInput = dropdown.querySelector(".document-date-input");

        textContainer.classList.remove("hidden");
        hiddenText.classList.add("hidden");
        hiddenModalTitle.classList.add("hidden");
        hiddenModalDesc.classList.add("hidden");
        btnSection.classList.add("hidden");
        visibleBtnSection.classList.remove("hidden");
        documentDateInput.classList.add("hidden");

        hiddenText.style.width = "";
    })
})
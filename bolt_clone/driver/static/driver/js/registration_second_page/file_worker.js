const fileInputs = Array.from(document.querySelectorAll("input[type='file']"));
const dropdownContainers = Array.from(document.querySelectorAll(".dropdown_modal"));
const closeButtons = Array.from(document.querySelectorAll(".close"));
const documentContainers = Array.from(document.querySelectorAll(".document-container"));


/*fileInputs.forEach((fileInput) => {
    fileInput.addEventListener("change", () => {
        if(fileInput.files.length > 0){
            const selectedFile = fileInput.files[0];
            let inputIndex = fileInputs.indexOf(fileInput);
            const reader = new FileReader();
            dropdownContainers[inputIndex].style.display = "block";
            reader.onload = (e) => {
                console.log("Here")
                console.log(e.target);
                documentContainers[inputIndex].innerHTML = `<img src="${e.target.result}" alt="Uploaded Document"
                style="width: 300px;"/>`
            }
            reader.readAsDataURL(selectedFile)
        }
    })
})
*/

fileInputs.forEach((fileInput) => {
    fileInput.addEventListener("change", () => {
        if(fileInput.files.length > 0){
            const selectedFile = fileInput.files[0];
            let inputIndex = fileInputs.indexOf(fileInput)
            dropdownContainers[inputIndex].style.display = "block";
            if(selectedFile.type === "application/pdf"){
                const reader = new FileReader();
                reader.onload = (e) => {
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
                            viewport: viewport,
                        };

                        const renderTask = page.render(renderContext);
                        renderTask.promise.then(() => {
                            const documentContainer = documentContainers[inputIndex];
                            documentContainer.innerHTML = `<img class="doc-image"
                            src="${canvas.toDataURL()}" alt="Uploaded Document"/>`;
                        })
                    })
                }
                reader.readAsArrayBuffer(selectedFile);
            } else if (selectedFile.type.startsWith("image/")){
                const reader = new FileReader();
                reader.onload = (e) => {
                    const documentContainer = documentContainers[inputIndex];
                    documentContainer.innerHTML = `<img class="no-doc-image"
                    src="${e.target.result}" alt="Uploaded Document"/>`;
                };
                reader.readAsDataURL(selectedFile);
            } else {
                console.error("Unsupported file type")
            }
        }
    });
});

closeButtons.forEach((closeBtn) => {
    closeBtn.addEventListener("click", () => {
        let btnIndex = closeButtons.indexOf(closeBtn);
        dropdownContainers[btnIndex].style.display = "none";
    })
})
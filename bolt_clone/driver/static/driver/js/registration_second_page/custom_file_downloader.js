document.addEventListener("DOMContentLoaded", () => {
    const fileUploadWrappers = document.querySelectorAll(".file-upload-wrapper");
    fileUploadWrappers.forEach(wrapper => {
        const fileInput = wrapper.querySelector("input[type='file']");
        console.log(wrapper);
        console.log(fileInput);
        const button = wrapper.querySelector(".custom-file-downloader");

        button.addEventListener("click", () => {
            fileInput.click();
        });
    })
})

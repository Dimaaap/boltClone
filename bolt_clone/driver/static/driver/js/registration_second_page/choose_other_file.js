const chooseOtherFileBtnArray = Array.from(document.querySelectorAll(".choose-other"));
const fileInputsArray = Array.from(document.querySelectorAll("input[type='file']"));


chooseOtherFileBtnArray.forEach(btn => {
    btn.addEventListener("click", () => {
        const btnIndex = chooseOtherFileBtnArray.indexOf(btn);
        fileInputsArray[btnIndex].click();
    })
})

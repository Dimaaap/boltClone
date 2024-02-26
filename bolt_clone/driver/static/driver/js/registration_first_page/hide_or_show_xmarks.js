const cancelMarks = Array.from(document.querySelectorAll(".fa-xmark"));
const inputsWithMarks = Array.from(document.querySelectorAll(".with-span"));


const hideXMarks = () => {
    cancelMarks.forEach((mark) => {
        mark.style.display = "none";
    })
}

const addOnClickListenerToXMarks = () => {
    cancelMarks.forEach((mark) => {
        mark.addEventListener("click", () => {
            const xMarkIndex = cancelMarks.indexOf(mark);
            inputsWithMarks[xMarkIndex].value = "";
            mark.style.display = "none";
        })
    })
}

const showXMarkInNonEmptyField = () => {
    inputsWithMarks.forEach((input) => {
        input.addEventListener("input", () => {
            const inputIndex = inputsWithMarks.indexOf(input);
            cancelMarks[inputIndex].style.display = "inline-block";
        })
    })
}

document.addEventListener("DOMContentLoaded", () => {
    hideXMarks();
    showXMarkInNonEmptyField();
    addOnClickListenerToXMarks();
})
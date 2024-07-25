const rangeInput = document.querySelectorAll(".range-input input"),
progress = document.querySelector(".slider .progress")

rangeInput.forEach(input => {
    input.addEventListener("input", ()=>{
        let minVal = parseInt(rangeInput[0].value),
        maxVal = parseInt(rangeInput[1].value);

        progress.style.left = (minVal / rangeInput[0].max) * 100 + "%";
        progress.style.right = (maxVal / rangeInput[1].max) * 100 + "%";
    });
});
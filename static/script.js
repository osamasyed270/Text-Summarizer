const textarea = document.querySelector(".textarea-container .textarea-inner-container textarea")
const textareaOverlay = document.querySelector(".textarea-container .textarea-inner-container .textarea-overlay-info")

textareaOverlay.addEventListener("click", function() {
    textarea.focus()
})


textarea.addEventListener("focus", function() {
    if (document.activeElement === textarea || textarea.value !== "") {
        textareaOverlay.style.display = "none"
    } else {
        textareaOverlay.style.display = "flex"
    }
})

textarea.addEventListener("blur", function() {
    if (document.activeElement === textarea || textarea.value !== "") {
        textareaOverlay.style.display = "none"
    } else {
        textareaOverlay.style.display = "flex"
    }
})
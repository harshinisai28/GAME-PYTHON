document.addEventListener("DOMContentLoaded", function() {
    const guessInput = document.getElementById("guess");
    const guessButton = document.getElementById("check");

    guessInput.addEventListener("keydown", function(event) {
        if (event.key === "Enter") {
            event.preventDefault();
            guessButton.click();
        }
    });
});
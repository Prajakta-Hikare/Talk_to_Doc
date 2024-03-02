const textArray = ["talk to a document...", "locally hosted...", "voice search...", "summarization..."];
let loopIndex = 0;
let characterIndex = 0;
let isTyping = true;

function typeWriter() {
    const typewriterText = document.getElementById("typewriter-text");

    if (isTyping) {
        typewriterText.innerHTML += textArray[loopIndex].charAt(characterIndex);
        characterIndex++;

        if (characterIndex === textArray[loopIndex].length) {
            isTyping = false;
            setTimeout(typeWriter, 1000);
        } else {
            setTimeout(typeWriter, 100);
        }
    } else {
        typewriterText.innerHTML = '';
        characterIndex = 0;
        loopIndex = (loopIndex + 1) % textArray.length;
        isTyping = true;
        setTimeout(typeWriter, 500);
    }
}

window.onload = typeWriter;


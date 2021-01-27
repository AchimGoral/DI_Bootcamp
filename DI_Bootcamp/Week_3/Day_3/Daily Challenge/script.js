let container = document.getElementById('text-container');
let input = document.getElementById('text-input');

input.addEventListener('keypress', keyLogger);

let letters = /^[A-Za-z]+$/;

function keyLogger(element) {
    if (element.key.match(letters)){
        container.textContent += `${element.key}`;
    } else {
        container.textContent += ``;
    }
}
// Clear button for text input field

let clearAllButton = document.querySelector('.btn-clear');
clearAllButton.addEventListener('click', clear);

let inputHeadline = document.querySelector(".form-control-headline");
let inputText = document.querySelector(".form-control-text");

function clear() {

    inputHeadline.value = "";
    inputText.value = "";
}

// Create new Blog card

let containerCard;
let divCard;
let divCardBody;
let cardTitle;
let breakLine;
let cardText;

function createCard () {
    containerCard = document.querySelector('.comments');

    divCard = document.createElement('div');
    divCardBody = document.createElement('div');
    cardTitle = document.createElement('h5');
    breakLine = document.createElement('hr');
    cardText = document.createElement('p');

    divCard.classList.add('card', 'card-comment');
    divCardBody.classList.add('card-body', 'card-body-comment');
    cardTitle.classList.add('card-title', 'card-title-comment');
    cardText.classList.add('card-text', 'card-text-comment');

    divCardBody.appendChild(cardTitle);
    divCardBody.appendChild(breakLine);
    divCardBody.appendChild(cardText);
    divCard.appendChild(divCardBody);
    containerCard.appendChild(divCard);
}

// Submit the post

let submitButton = document.querySelector(".btn-submit");

submitButton.addEventListener("click", addContent);

function addContent () {

    let headlineField = document.querySelector(".form-control-headline").value;
    let textField = document.querySelector(".form-control-text").value;

    if (inputHeadline.value == "" || inputText.value == "") {
        alert("Text fields can't be empty");
        return; // checks for empty input and leaves the function if empty
    } else {
        createCard();

        let headline = document.createTextNode(headlineField);
        cardTitle.appendChild(headline);
    
        let text = document.createTextNode(textField);
        cardText.appendChild(text);
    
        clear(); // clears the text fields after submitting
    }
}
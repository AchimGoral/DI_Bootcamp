// Exercise_1

let articleSelect = document.getElementsByTagName('p');
for (let i = 0; i < articleSelect.length; i++) {
    articleSelect[i].classList.add('para_article'); 
}

let lastParagraph = document.body.firstElementChild.lastElementChild;

lastParagraph.remove();

let h2_delete = document.querySelector('h2');
h2_delete.addEventListener("click", delete_h2);

function delete_h2 (event) {
    event.target.remove();
}

let size = Math.floor(Math.random() * 101).toString();
let pixel = "px";
let sizeString = size.concat(pixel);

document.body.firstElementChild.firstElementChild.style.fontSize = sizeString;

let firstParagraph = document.body.firstElementChild.children[2];

firstParagraph.addEventListener("click", paragraph_delete);

function paragraph_delete (event) {
    event.target.style.display = "none";
}

let newTable = document.createElement("table");

document.body.firstElementChild.appendChild(newTable);

let input_left = document.body.children[1].children[1];

let input_right = document.body.children[1].children[3];

input_left.onchange = function() {
    let newRow = document.createElement("tr");
    newTable.appendChild(newRow);
    newRow.innerHTML = input_left.value;
};

input_right.onchange = function() {
    let newRow = document.createElement("tr");
    newTable.appendChild(newRow);
    newRow.innerHTML = input_right.value;
};
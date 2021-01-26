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

document.body.firstElementChild.firstElementChild.style.fontSize = size + "px";

let firstParagraph = document.body.firstElementChild.children[2];

firstParagraph.addEventListener("click", paragraph_delete);

function paragraph_delete (event) {
    event.target.style.display = "none";
}

let newTable = document.createElement("table");
document.body.firstElementChild.appendChild(newTable);

let input_left = document.forms[0].userName;

let input_right = document.forms[0].questionToUser;

input_left.onchange = function() {
    let row = newTable.insertRow(0);
    let cell1 = row.insertCell(0);
    cell1.innerHTML = input_left.value;
};

input_right.onchange = function() {
    let row = newTable.insertRow();
    let cell2 = row.insertCell(0);
    cell2.innerHTML = input_right.value;
};
// // Part 1

// let bodyWebsite = document.body;
// let divWebsite = bodyWebsite.firstElementChild;
//                             // .children[0]

// let ulWebsite = divWebsite.firstElementChild;

// let liThirdWebsite = ulWebsite.lastElementChild;
//                             // .children[2]

// liThirdWebsite.textContent = 'John';

// let liSecondWebsite = liThirdWebsite.previousElementSibling;

// liSecondWebsite.textContent = 'Signed In';

// // Part 2

// let bodyWebsite = document.body;
// let divWebsite_1 = bodyWebsite.firstElementChild.textContent;
// let divWebsite_2 = bodyWebsite.children[0].textContent;

// console.log(divWebsite_1);
// console.log(divWebsite_2);

// let ilWebsite_1 = bodyWebsite.children[1].lastElementChild;

// console.log(ilWebsite_1.textContent);

// let ulWebsite_1 = ilWebsite_1.parentNode;
// let ulWebsite_2 = bodyWebsite.children[1];

// console.log(ulWebsite_1);
// console.log(ulWebsite_2);

// Part 3

let divWebsite = document.getElementById('usersTitle');
console.log('div: ', divWebsite);

let listWebsite = document.getElementsByClassName('username');
console.log('username: ', listWebsite);

console.log('1. username: ', listWebsite[0]);

let bodyWebsite = document.body;
let newDiv = document.createElement("div");

for (let i = 0; i < 5; i++) {
    let newParagraph = document.createElement("p");
    newParagraph.className = "paragraph";
    let newContent = document.createTextNode("Hello new user " + (i+1));
    newParagraph.appendChild(newContent);
    newDiv.appendChild(newParagraph);
}

bodyWebsite.appendChild(newDiv);

// // newDiv.setAttribute("class", "newDiv");
// // newDiv.className = "newDiv"; // overrides if another class is added

// newDiv.classList.add("newdiv", "olddiv");
// newDiv.classList.toggle("newdiv", false); // deletes class
// newDiv.style.color = "blue";

// let newParagraph = document.createElement("p");

// let newContent = document.createTextNode("Hello new users");

// // Add content to Paragraph
// newParagraph.appendChild(newContent);

// // Add the paragraph to the div
// newDiv.appendChild(newParagraph);

// // Add the div to the body
// bodyWebsite.appendChild(newDiv);
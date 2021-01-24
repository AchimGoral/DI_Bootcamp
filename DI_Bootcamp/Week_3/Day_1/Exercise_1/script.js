//  Exercise_1

let bodyWebsite = document.body;

let newNavBar = bodyWebsite.firstElementChild.setAttribute("id", "socialNetworkNavigation");

let newLiTag = document.createElement("li");

let newContent = document.createTextNode("Logout");

let divTag = bodyWebsite.firstElementChild;

let ulTag = divTag.firstElementChild;

let liTag = ulTag.firstElementChild;

newLiTag.appendChild(newContent);

ulTag.appendChild(newLiTag);


// Bonus Exercise_1

for (let i = 0; i < 6; i++) {
    console.log(ulTag.children[i].textContent);
}

// Exercise_2

let bodyWebsite = document.body;

let ulTag_1 = bodyWebsite.children[1];

let liTag_2 = ulTag_1.children[1];

liTag_2.innerHTML = "Richard";

let ulTag_item = document.getElementsByClassName("list");

for (let i = 0; i < ulTag_item.length; i++) {
    ulTag_item[i].firstElementChild.innerHTML = "Achim";
}


for (let i = 0; i < ulTag_item.length; i++) {
    let newLiTag_2 = document.createElement("li");

    let newContent_2 = document.createTextNode("Hey Students");

    newLiTag_2.appendChild(newContent_2);

    ulTag_item[i].appendChild(newLiTag_2);
}

let ulTag_3 = document.getElementsByClassName("list")[1];

let ilTag_3 = ulTag_3.children[1];

ulTag_3.removeChild(ilTag_3);

// Exercise_3

// Self-learning

// Exercise_4

document.body.firstElementChild.style.backgroundColor = "lightblue";

document.body.children[1].firstElementChild.innerHTML = "";

document.body.children[1].lastElementChild.style.border = "1px solid black";

document.body.style.fontSize = "x-large";
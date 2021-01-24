// //  Exercise_1

// let bodyWebsite = document.body;

// let newNavBar = bodyWebsite.firstElementChild.setAttribute("id", "socialNetworkNavigation");

// let newLiTag = document.createElement("li");

// let newContent = document.createTextNode("Logout");

// let divTag = bodyWebsite.firstElementChild;

// let ulTag = divTag.firstElementChild;

// let liTag = ulTag.firstElementChild;

// newLiTag.appendChild(newContent);

// ulTag.appendChild(newLiTag);


// // Bonus Exercise_1

// for (let i = 0; i < 6; i++) {
//     console.log(ulTag.children[i].textContent);
// }

// Exercise_2

let bodyWebsite = document.body;

let ulTag_1 = bodyWebsite.children[1];

let liTag_2 = ulTag_1.children[1];

liTag_2.innerHTML = "Richard";

let ulTag_item1 = document.getElementsByClassName("list");

for (let i = 0; i < ulTag_item1.length; i++) {
    ulTag_item1[i].firstElementChild.innerHTML = "Achim";
}


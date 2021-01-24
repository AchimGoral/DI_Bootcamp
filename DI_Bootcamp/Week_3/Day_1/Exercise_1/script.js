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

for (let i = 0; i < 6; i++) {
    console.log(ulTag.children[i].textContent);
}
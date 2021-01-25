// function clickParagraph() {
//     document.getElementById("paragraph").classList.toggle("welcomeUser");
//     document.getElementById("paragraph").style.backgroundColor = "yellow";
// }

// // Table Exercise

// function insert_Row() {
//     let newRow = document.createElement("tr");
//     let tableAccess = document.getElementById("sampleTable"); // Access to the table
//     for (let i = 0; i < 2; i++) {
//         let newLine = document.createElement("td");
//         let newContent = document.createTextNode(`New row cell${i+1}`);
//         newLine.appendChild(newContent);
//         newRow.appendChild(newLine);
//     }
//     tableAccess.appendChild(newRow);
// }

// // Event listener

// let paragraph = document.getElementById("para");
// paragraph.addEventListener("click", clickParagraph);

// let listShopping = document.getElementById("list");
// listShopping.addEventListener("click", clickParagraph);

// function clickParagraph (event) {
//     event.target.style.backgroundColor = "yellow";
//     console.log(event);
// }

// Exercise 2

let button = document.getElementById('jsstyle');
button.addEventListener("click", click);
button.addEventListener("mouseover", background);
button.addEventListener("mouseout", innerText);

function click () {
    alert("You clicked the button");
}

function background (event) {
    event.target.style.backgroundColor = "yellow";
}

function innerText (event) {
    event.target.innerHTML = "Hello";
}
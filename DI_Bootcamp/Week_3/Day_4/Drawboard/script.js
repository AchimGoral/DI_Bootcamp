
for (let i = 0; i < (80*48); i++) {
    let divContainer = document.createElement('div');
    document.getElementById('gridPad').appendChild(divContainer);
    divContainer.style.backgroundColor = "black";
}           // Creating the grid-layout with a field size of 80*48

let colorDiv = null; // Empty variable for color in div
let mousedown = false; // Boolean for mousedown event
let clear = document.getElementById('button-reset');
let sidebar_color = document.querySelectorAll('#sidebar > div');
let grid_fill = document.querySelectorAll('#gridPad > div');
let body = document.getElementsByTagName('body')[0];

body.addEventListener("mousedown", function(){
    mousedown = true;
});

body.addEventListener("mouseup", function(){
    mousedown = false;
});

for(sidebar_color of sidebar_color) {
    sidebar_color.addEventListener("click")
}

clear.addEventListener("click", function(){
    for (grid_fill of grid_fill) {
        grid_fill.style.backgroundColor = "white";
    }
});
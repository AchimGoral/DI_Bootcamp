function getBold_items () {
    let boldItems = document.querySelectorAll("strong");
    return boldItems;
}

function highlight() {
    let colorItems = getBold_items();
    for (let i = 0; i < colorItems.length; i++) {
        colorItems[i].style.color = "blue";
      }
}

function return_normal () {
    let returnBlack = getBold_items();
    for (let i = 0; i < returnBlack.length; i++) {
        returnBlack[i].style.color = "black";
      }
}

document.addEventListener("mouseover", highlight);
document.addEventListener("mouseout", return_normal);

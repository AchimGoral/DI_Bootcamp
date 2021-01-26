// let container = document.getElementById('container');
let animate = document.getElementById('animate');

function myMove() {
    let position = 0;
    let interval = setInterval(makeItMove,10);
    function makeItMove() {
      if (position == 350) {
        clearInterval(interval);
      }
      else {
        position++;
        animate.style.left = position + "px";
      }
    }
}

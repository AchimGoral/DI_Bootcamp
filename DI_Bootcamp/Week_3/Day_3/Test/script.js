// // Timeout

// function sayHi(message) {
//   let container = document.getElementById("container");
//   Object.assign(container.style,{
//     backgroundColor: "lightblue",
//     fontSize: "50px",
//     padding: "5px 10px",
//     border: "1px solid darkblue",
//     width: "max-content",
//     fontFamily: "Lucida sans",
//     margin: "auto"
//   });
//   container.textContent = message;
// }

// setTimeout(sayHi, 5000, "The sales end in 10min ! ");

// // Interval

// function sayHi() {
//   console.log("Interval log");
// }

// function stopTimer () {
//   clearInterval(timing);
// }

// // setInterval(sayHi, 2000);

// let hello = document.getElementById("container");
// let bye = document.getElementsByClassName("containerbye")[0];

// let timing = setInterval(sayHi, 20);

// bye.addEventListener("click", stopTimer);

// Exercise_2

function sayHi(message) {
  let container = document.getElementById("container");
  Object.assign(container.style,{
    backgroundColor: "lightblue",
    fontSize: "50px",
    padding: "5px 10px",
    border: "1px solid darkblue",
    width: "max-content",
    fontFamily: "Lucida sans",
    margin: "auto"
  });
  container.textContent = message;
}

setTimeout(sayHi, 2000, `The sales end in ${i}min ! `);

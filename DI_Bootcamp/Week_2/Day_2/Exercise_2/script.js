// Exercise_1

let language = prompt("Which language do you speak?");

if (language == "english") {
    alert("Hello there");
} else if (language == "french") {
    alert("Bonjour");
} else if (language == "hebrew") {
    alert("שלום");
} else {
    alert("01110011 01101111 01110010 01110010 01111001");
}

// Exercise_2

let grade = prompt("What is your grade? on a scale of 0 - 100");

if (grade > 90) {
    alert("A");
} else if (grade <= 90 && grade > 80) {
    alert("B");
} else if (grade <= 80 && grade >= 70) {
    alert("C");
} else{
    alert("D");
}

// Exercise_3

let verb = prompt("choose a verb");

let verbLength = verb.length;

let add1 = "ing";
let add2 = "ly";

if (verbLength < 3) {
    alert(verb);
} else if (verbLength >= 3 && verb.includes("ing")) {
    alert(verb.concat(add2));
} else {
    alert(verb.concat(add1));
}
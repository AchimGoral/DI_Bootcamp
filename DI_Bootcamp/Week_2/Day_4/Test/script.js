// function age (myAge) {
//     let ageMom = 2*myAge;
//     let ageDad = 1.2*ageMom;
//     console.log(`My mum is ${ageMom} years old and my dad is ${ageDad} years old`);
// }

// age(26);

let myAge = prompt(`What is your age?`);

function ageOfMom () {
    let ageMom = 2*myAge;
    return ageMom;
}

console.log(`My mom is ${ageOfMom(myAge)} years old`);
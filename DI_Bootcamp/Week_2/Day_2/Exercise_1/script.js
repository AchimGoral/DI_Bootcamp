// Exercise_1

let x = 5;
let y = 2;

if ( x > y) {
    console.log("X is the biggest number");
} else {
    console.log("y is the biggest number");
}

// Exercise_2

let newDog = "Chihuahua";

console.log(newDog.length);

// Exercise_3

// let z = prompt("Choose your integer");

// if (z%2 == 0) {
//     alert(`${z} is an even number`);
// } else {
//     alert(`${z} is an odd number`);
// }

// Exercise_4

let users = ["Lea123", "Princess45", "cat&doglovers", "helooo@000"];

console.log(users);

if (users.length == 0) {
    console.log('no one is online');
} else if (users.length == 1) {
    console.log(`${users[0]} is online`);
} else if (users.length == 2) {
    console.log(`${users[0]} and ${users[1]} are online`);
} else {
    console.log(`${users[0]} and ${users[1]} and ${users.length-2} are online`);
}
// Exercise_1

let colors = ["blue", "red", "green"];
let suffix = [".st", ".nd", ".rd"];

for (i = 0, j = 1; i, j <= colors.length; i++, j++) {
    console.log(`My ${j}${suffix[i]} choise is ${colors[i]}`);
}

// Exercise_2

let people = ["Greg", "Mary", "Devon", "James"];

for (i = 0; i < people.length; i++) {
    console.log(people[i]);
}

var index = people.indexOf("Greg");

if (index !== -1) {
    people.splice(index, 1);
}
console.log(people);

var index = people.indexOf("James");

if (index !== -1) {
    people.splice(index, 1, "Jason");
}

console.log(people);

people.push("Achim");

console.log(people);

var index = people.indexOf("Jason");

for(i = 0; i < people.length; i++) {

    console.log(people[i]);

    if (i == index) {
        break;
    }
}

var index_2 = people.indexOf("Achim");

let people_2 = people.slice(index-1, index_2);

console.log(people_2);

console.log(people.indexOf("Mary"));

console.log(people.indexOf("Foo"));

let last = people[people.length-1];

console.log(last);

// Exercise_3

let number = prompt("Pick a number");

while (number < 10) {
    alert("The number must be bigger then 10");
    number = prompt("Pick a number");
}

alert(`Your number is: ${number}`);

// Exercise_4

let guestList = {
    Randy: "Germany",
    Karla: "France",
    Wendy: "Japan",
    Norman: "England",
    Sam: "Argentina"
};

console.log(guestList);

let guest = prompt(`What is your Name?`);


for (const i in guestList) {
    if (guest != i) {
        continue;
    } else if (guest == i){
        alert(`Hi! I'm ${i}, and I'm from ${guestList[i]}.`);
        break;
    } else {
        alert(`Hi, I am a guest`);
        break;
    }
}

// Exercise_5

let family = {
    children: 5,
    mother: "Anna",
    car: "Mazda",
    country: "England",
    number: "12"
};

for (const i in family) {
    console.log(i);
}

console.log("-----------");

for (const j in family) {
    console.log(family[j]);
}

// Exercise_6

let names = ["Jack", "Philip", "Sarah", "Amanda", "Bernard", "Kyle"];

let sortedNames = names.sort();
let newList = "";

for (const i in sortedNames) {
    newList += sortedNames[i][0];
}

console.log(newList);
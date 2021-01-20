let fruits = ["Banana", "Apples", "Oranges", "Blueberries"];

fruits.shift();

fruits.sort();

fruits.push("Kiwi");

fruits.splice(0, 1);

fruits.reverse();

console.log(fruits);

let moreFruits = ["Banana", ["Apples", ["Oranges"], "Blueberries"]];

let oranges = moreFruits[1][1][0];

console.log(oranges);
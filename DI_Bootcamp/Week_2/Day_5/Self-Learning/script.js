// Exerecise_1

var num = 8;
var num = 10;
console.log(num);

// Expected output: num == 10, because the last last value overrites the previous ones.

// Exercise_2

function numbers() {
let i;
for (i = 0; i < 5; i++) {
    console.log(i);
}
    console.log(i);
}
numbers();

//Exercise_3

let moneyAccount = 10000;
console.log(`Expenses before spendings: ${moneyAccount}`);

const vat = 0.15;
let expenses = 3000;
console.log(`Amount of expenses: ${expenses}. Tax is ${vat*100}%`);

let vatAmount = expenses*vat;

moneyAccount -= (expenses-vatAmount);

console.log(`Expenses after spendings: ${moneyAccount}`);
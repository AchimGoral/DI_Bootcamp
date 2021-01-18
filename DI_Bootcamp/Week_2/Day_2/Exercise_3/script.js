// Exercise_1

let year_1 = prompt("Give me your first Year");

let year_2 = prompt("Give me your second Year");

let year_now = prompt("Give the actual year");

let age_1 = year_now - year_1;
let age_2 = year_now - year_2;

while (age_1 > 2*age_2) {
    age_1--;
    age_2--;
    return age_1, age_2;
}

console.log(age_1, age_2);
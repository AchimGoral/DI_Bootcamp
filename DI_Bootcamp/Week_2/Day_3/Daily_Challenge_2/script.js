// // Part_1

// let numbers = [5,0,9,1,7,4,2,6,3,8];

// console.log(numbers.toString());

// numbers = [5,0,9,1,7,4,2,6,3,8];

// console.log(numbers.join());

// numbers = [5,0,9,1,7,4,2,6,3,8];

// console.log(numbers.join(''));

// numbers = [5,0,9,1,7,4,2,6,3,8];

// console.log(numbers.join(' '));

// numbers = [5,0,9,1,7,4,2,6,3,8];

// console.log(numbers.join('-'));

// // Part_2

let numbers = [5,0,9,1,7,4,2,6,3,8];

for (let i = 0; i < numbers.length; i++) {
    console.log(numbers);
    for (let j = 0; j < numbers.length; j++) {
        console.log(numbers);
        if (numbers[i] > numbers[j]) {
            let temp = numbers[i];
            numbers[i] = numbers[j];
            numbers[j] = temp;
        }
    }
}

console.log(numbers);
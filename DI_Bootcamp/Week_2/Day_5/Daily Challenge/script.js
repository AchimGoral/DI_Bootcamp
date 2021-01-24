let sum = prompt(`How many bottels of beer?`);

while (isNaN(sum) == true) {        // Check for Int
    sum = prompt(`How many bottels of beer?`);
}

let count = 1; // Counter for beer

console.log("===============================");
while(sum > 1) {

    console.log(`${sum} bottels of beer on the wall`);
    console.log(`${sum} bottels of beer on the wall`);
    console.log(`${sum} bottels of beer`);

    if (count == 1) {               // One-time statement for the first bottle
        console.log(`Take ${count} down, pass it around`);
    } else if (count > sum) {       // If the amount of bottles to take down is bigger than the sum, take down the sum
        console.log(`Take ${sum} down, nothing to pass around`);
    } else {
        console.log(`Take ${count} down, pass them around`);
    }
    
    sum -= count;
    count++;
}

console.log(`0 bottels of beer on the wall`);
console.log(`Go home, you're drunk!!!`);
console.log("===============================");
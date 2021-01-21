let sumStr = prompt(`How many bottels of beer?`);
let sum = parseInt(sumStr);

let count = 1; // COunter for beer

// let sentence_1 = (`${sum} bottels of beer on the wall`);
// let sentence_2 = (`${sum} bottels of beer`);
// let sentence_3 = (`Take ${count} down, pass it around`);
// let sentence_4 = (`Take ${count} down, pass them around`); // SOmehow not working, when passed into the logs, any suggestions?

console.log("===============================");
while(sum > 1) {
    console.log(`${sum} bottels of beer on the wall`);
    console.log(`${sum} bottels of beer on the wall`);
    console.log(`${sum} bottels of beer`);
    if (count == 1) {
        console.log(`Take ${count} down, pass it around`);
    } else {
        console.log(`Take ${count} down, pass them around`);
    }
    sum -= count;
    count++;
}

console.log(`0 bottels of beer on the wall`);
console.log(`That's it go home`);
console.log("===============================");
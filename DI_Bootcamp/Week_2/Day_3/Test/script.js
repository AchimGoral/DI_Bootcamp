// //Exercise_1

// for(let i = 0; i <=15; i++) {
//     if (i%2 == 0) {
//         console.log(`${i} is an even number`);
//     } else {
//         console.log(`${i} is an odd number`);
//     }
// }

// // Exercise_2

let names= ["john", "sarah", 23, "Rudolf",34];

for (const i in names) {
    if(typeof(names[i]) != "string") {
        continue;
    } else {
        console.log(names[i]);
    }
}

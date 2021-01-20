// Daily_Challenge

let stars;

for (let i = 0; i <= 6; i++) {
    for (let j = 0; j <= i; j++) {
        stars = "*".repeat(j);
        // console.log(stars);
    }
    console.log(stars);
}
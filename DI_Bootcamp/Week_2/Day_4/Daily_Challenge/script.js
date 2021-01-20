let sentence = prompt(`Give me a sentence with space seperated words`);

let sentenceArray = sentence.split(' ');

let starLeft = '* ';
let starRight = ' *';
let space = " ";
let temp = 0;

function stars (){

    for(let i = 0; i < sentenceArray.length; i++) {
        if (temp < sentenceArray[i].length) {
            temp = sentenceArray[i].length;
        }
    }
    
    temp +=4; // Value for the lenght of the stars and 2 spaces and 2 outside stars
    let star = "*";
    for (let i = 0; i < temp; i++) {
        star += "*";
    }
    console.log(star); // Upper line of stars
    for(let i = 0; i < sentenceArray.length; i++) {
        let difference = temp-sentenceArray[i].length-3; // Subtracting from the temp lenght the lenght for each word and -3 because of the outside adition for star and counting from 0
        console.log(starLeft+sentenceArray[i]+space.repeat(difference)+starRight);
    }
    console.log(star); // Down line of stars
}

stars();
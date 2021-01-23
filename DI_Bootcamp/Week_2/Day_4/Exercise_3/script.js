// Exercise_1

function random () {
    let randomNumber = Math.floor(Math.random() * 101);
    return randomNumber;
}

function evenNumbers () {
    let randomNumberPass = random ();
    let numberList = [];

    for (let i = 0; i <= randomNumberPass; i++) {
        numberList.push(i);
    }

    let finalList = [];
    for (let i = 0; i <numberList.length; i++) {
        if (numberList[i]%2 == 0) {
            finalList.push(i);
        } else {
            continue;
        }
    }
    return finalList;
}


console.log(evenNumbers());

// Exercise_2 // Not ready/working

function capitalize (array) {
    let newString = [];

    for (let i = 0; i < array.length; i++) {
        if (array[i].length%2 == 0) {
            newString[i] = array[i].toUpperCase();
        } else {
            newString[i] = array[i].toLowerCase();
        }
    }

    return newString;
}

console.log(capitalize("hallo"));

// Exercise_3

function palyndrome (array) {
    let varLen = array.length;
    for (let i = 0; i < varLen/2; i++) {
        if (array[i] !== array[varLen-1-i]) {
            return console.log(`The word ${array} isn't a palyndrome. Try again`);
        }
    }
    return console.log(`The word ${array} is a palyndrome. Congratulations`);
}

let array = prompt(`Which word to check for palyndrome?`);

palyndrome(array);

// Exercise_4

function randomArray () {
    let arrayPrompt = prompt("How long should your array be?");
    while (isNaN(arrayPrompt) == true) {
        arrayPrompt = prompt("How long should your array be?");
    }

    let countNumber = prompt(`Until which number should your array count?`);
    while (isNaN(countNumber) == true) {
        countNumber = prompt("Until which number should your array count?");
    }

    let arrayNumber = [];

    for ( let i = 0; i < arrayPrompt; i++) {
        arrayNumber.push(Math.floor(Math.random() * countNumber+1));
    }

    console.log(arrayNumber);
    return arrayNumber;
}


function biggestNumberInArray () {
    let newArray = randomArray();
    let temp = [];

    for (let i = 0; i < newArray.length; i++) {
        
        if (isNaN(newArray[i]) == true) {
            break;
        } else if (newArray[i] > temp) {
            temp = newArray[i];
        } else {
            continue;
        }
    }

    return temp;
}

console.log(biggestNumberInArray());

// Exercise_5

function randomArray () {
    let arrayPrompt = prompt("How long should your array be?");
    while (isNaN(arrayPrompt) == true) {
        arrayPrompt = prompt("How long should your array be?");
    }

    let countNumber = prompt(`Until which number should your array count?`);
    while (isNaN(countNumber) == true) {
        countNumber = prompt("Until which number should your array count?");
    }

    let arrayNumber = [];

    for ( let i = 0; i < arrayPrompt; i++) {
        arrayNumber.push(Math.floor(Math.random() * countNumber+1));
    }

    console.log(arrayNumber);

    return arrayNumber;           // Same function for creating random array like in Exercise_4
}

function doubleValues () {
    let arrayInhertited = randomArray();
    let newArray = [];

    for (let i = 0; i < arrayInhertited.length-1; i++) {
        if(newArray.indexOf(arrayInhertited[i]) === -1) {
            newArray.push(arrayInhertited[i]);
        }
    }
    return newArray;
}

console.log(doubleValues());
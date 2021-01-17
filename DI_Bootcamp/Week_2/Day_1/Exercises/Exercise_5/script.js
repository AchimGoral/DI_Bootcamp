let text = 'I am finding Nemo !';

console.log(text);

let splitted = text.split(' ');

let found = splitted.indexOf('Nemo');

if (found == -1) {
    console.log(`I couldn't find Nemo`); 
}

else {
    console.log(`I found Nemo at Index: ${found + 1}`); // +1 for the counting convention starting with 0
}
let sentence = prompt("Write a sentence with not first and bad later. Or a sentence with good inside");

let searchNot = sentence.search("not");
let searchBad = sentence.search("bad");


let good = "good";

if (searchNot == -1 && searchBad == -1) {
    alert(sentence);
} else if (searchNot > searchBad) {
    alert(sentence);
} else {
    let midSent1 = sentence.slice(0, searchNot);
    let finalSent = midSent1.concat(good);
    alert(finalSent);
}
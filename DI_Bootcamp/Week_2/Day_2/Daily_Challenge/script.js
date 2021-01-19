let sentence = prompt("Write a sentence with not first and bad later. Or a sentence with good inside");

let searchNot = sentence.search("not");
let searchBad = sentence.search("bad");
let good = "good";

if ((searchNot == -1 && searchBad == -1) || (searchNot > 0 && searchBad == -1) || (searchNot == -1 && searchBad > 0) || (searchNot > searchBad)) {
    alert(sentence);
} else {
    let finalSent = sentence.slice(0, searchNot).concat(good)+sentence.slice(searchBad+3);
    alert(finalSent);
}
// The movie was not so very bad, I liked it!
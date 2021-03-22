// Get Elements
const search = document.querySelector('#search');
const matchList = document.querySelector('#match-list');

// Searc JSON Airport file
const searchFlights = async searchText => {
    const response = await fetch('airports.json');
    const data = await response.json();

    // Filter Data with regex
    let results = data.filter(result => {
        const regexIata = new RegExp(`^${searchText}`, 'gi');
        const regexName = new RegExp(`${searchText}`, 'gi');
        if (result.name != null) {
            return result.iata.match(regexIata) || result.name.match(regexName);
        }
    });

    if (searchText.length === 0) {
        matches = []; // Empty array if no result
        matchList.innerHTML = ''; // Shows nothing when searchbar is empty
    }

    else {
        outputHtml(results);
        console.log(results);
    }
};

const outputHtml = results => {
    if(results.length > 0) {
        const html = results.map(match =>
            `<div class="card card-body mb-1">
                <a class="data-input"><h6>${match.iata} | ${match.name}</h6></a>
            </div>`).join('');

        matchList.innerHTML = html;
    }
};

// Event listern on any event, can also be key up, down or whatever
let timer;
search.addEventListener('input', () => {
  if(timer) clearTimeout(timer);
  timer = setTimeout(searchFlights, 100, search.value);
});

document.addEventListener('click', (e) => {
  if(e.target.classList.contains('.data-input')){
    search.value = e.target.textContent;
    document.querySelector('#match-list').innerHTML = "";
  }
});
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
        matchList.innerHTML = ''; // Shows nothing when serachbar is empty
    }

    else {
        outputHtml(results);
    }
};

const outputHtml = results => {
    if(results.length > 0) {
        const html = results.map(match =>
            `<div class="card card-body mb-1">
                <a href="#" class="data-input"><h6>${match.iata} | ${match.name}</h6></a>
            </div>`).join('');

        matchList.innerHTML = html;
    }
};

// Event listern on any event, can also be key up, down or whatever
search.addEventListener('input', () => searchFlights(search.value));

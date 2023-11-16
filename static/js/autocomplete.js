// Mapping div IDs to user-friendly titles
let divTitles = {
    "clean-energy": "Energy",
    "clean-water": "Water",
    "decent-work": "Work",
    "food-waste": "Food",
    "childbirth": "Childbirth",
    "hiv": "HIV Awareness",
    "medical-doctors-vs-nursing": "Medical Doctors vs. Nursing",
    "industry-innovation": "Industry",
    "public-transporation": "Sustainable Transportation",
    "quality-education": "Education",
    "overweight-stunting": "Overweight & Stunting",
    "zero-hunger-child-stunting": "Zero Hunger & Child Stunting"
};

function autocompleteSearch(searchText) {
    let divIds = Object.keys(divTitles);

    let matches = divIds.filter(divId => {
        return divId.toLowerCase().startsWith(searchText.toLowerCase());
    });

    displayMatches(matches);
}

function displayMatches(matches) {
    let outputHtml = matches.map(match => `<div onclick="selectDiv('${match}')">${divTitles[match]}</div>`).join('');
    document.getElementById("autocomplete-list").innerHTML = outputHtml;
}

function selectDiv(divId) {
    document.getElementById("searchBar").value = divTitles[divId];
    // Scroll to the div
    document.getElementById(divId).scrollIntoView();
    document.getElementById("autocomplete-list").innerHTML = '';
}

function clearSearch() {
    document.getElementById("searchBar").value = '';
    document.getElementById("autocomplete-list").innerHTML = '';
}

function performSearch() {
    let searchText = document.getElementById("searchBar").value;
    if (searchText) {
        // Searching for text placeholder
        console.log("Searching for:", searchText);
        // Call a function to search or simply use the searchText to filter or find data
    } else {
        console.log("Please enter a search term.");
    }
}

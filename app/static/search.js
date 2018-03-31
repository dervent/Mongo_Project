/**
 * Client-Side JavaScript
 */

function searchForDocs() {
    // Get text from search bar
    var searchText = document.getElementById("searchBar").value.split(/\s+/);

    // Form URL query
    var url = 'http://127.0.0.1:5000/search?text=';
    for(var i in searchText) {
        url += "+" + searchText[i];
    }
    // Future URL example to take in filter and sort parameters
    // http://127.0.0.1:5000/search?text=test+something&filter=description&sort=duration

    // Make AJAX call to server
    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function () {
        if(this.readyState == 4 && this.status == 200) {
            document.getElementById('results').innerHTML =
            this.response;
        }
    };
    xhttp.open("GET", url, true);
    xhttp.send();
}

function openDetailsModal(docId) {
    //ajax request to get information for that doc ID
}
function addComment() {
    // When the user adds comment, make a POST request
}

function goBackToTop() {
    // A "Back to Top" button will be displayed on the homepage.
    // When the user scrolls far down and clicks on the button, they should go to the top of the page.
}
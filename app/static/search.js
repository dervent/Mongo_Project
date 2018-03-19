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
            document.getElementById('desc1').innerHTML =
            this.response;
        }
    };
    xhttp.open("GET", url, true);
    xhttp.send();
}
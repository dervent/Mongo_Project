/**
 * Client-Side JavaScript
 */

function searchForDocs() {
    // Get text from search bar
    var searchText = document.getElementById("searchBar").value.split(/\s+/);

    // Form URL query
    var qurl = 'http://127.0.0.1:5000/search?text=';
    for(var i in searchText) {
        qurl += "+" + searchText[i];
    }
    // Future URL example to take in filter and sort parameters
    // http://127.0.0.1:5000/search?text=test+something&filter=description&sort=duration

    $.ajax(
    {
     url: qurl,
     type:"GET",
     async:true,
     success:function(result){
         console.log("jquery is here");
         $('#results')[0].innerHTML = result;
     }
    }
    );
    // Make AJAX call to server
    // var xhttp = new XMLHttpRequest();
    // xhttp.onreadystatechange = function () {
    //     if(this.readyState == 4 && this.status == 200) {
    //         console.log("hereeeee");
    //         $('#results')[0].innerHTML =
    //         this.response;
    //     }
    // };
    // xhttp.open("GET", url, true);
    // xhttp.send();
}

function openModal(eleID){
    //ajax GET request information for that ele ID
    //modal inner html = this.response
    //modal.show
    var qurl = 'http://127.0.0.1:5000/search?id='+eleID;
    $.ajax(
    {
     url: qurl,
     type:"GET",
     async:true,
     success:function(result){
         //the result will be a fully made modal (dialog tag)
         //get the results div and append the dialog tag
         $('#results')[0].append(result);
         //store dialog tag in a variable
         dialogEle = $('dialog')[0];
         //dialogEle.show()
         //THERE NEEDS TO BE A BUTTON IN THE DIALOAG that will call closeModal() function
         console.log("jquery is here");
     }
    }
    );

    console.log(eleID);
}

function closeModal(){
    //get the dialog tag from the DOM
    //this could be done inline....but thats kinda gross
    dialogEle = $('dialog')[0];
    //dialog.close()

}
function addComment() {
    // When the user adds comment, make a POST request
    var url = 'http://127.0.0.1:5000/comment';

}


function goBackToTop() {
    // A "Back to Top" button will be displayed on the homepage.
    // When the user scrolls far down and clicks on the button, they should go to the top of the page.
    $(window).scrollTop(0);
    console.log("back to top");
}

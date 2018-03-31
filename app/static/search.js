/**
 * Client-Side JavaScript
 */

 function searchForDocs() {
     // Get text from search bar
     var jsonObj = new Object();
     jsonObj.text = document.getElementById("searchBar").value;

     var filterVal = $('input[name=filters]:checked').val();
     var sortVal = $('input[name=sorts]:checked').val();

     if(typeof filterVal != 'undefined') jsonObj.filter = filterVal;
     if(typeof sortVal != 'undefined') jsonObj.sort = sortVal;

     var qurl = 'http://127.0.0.1:5000/search';

     $.ajax(
     {
      url:qurl,
      type:"GET",
      async:true,
      data:jsonObj,
      success:function(result){
          console.log("jquery is here");
          $('#results')[0].innerHTML = result;
      }
     }
     );
 }


function openModal(eleID){
    var jsonObj = new Object();
    jsonObj.id = eleID;
    qurl = 'http://127.0.0.1:5000/modal';
    $.ajax(
    {
     url:qurl,
     type:"GET",
     async:true,
     data:jsonObj,
     success:function(result){
              // the result will be a fully made modal
              // get the results div and append the modal. It will default as shown
              $('#results')[0].append(result);
     }
    }
    );
}
function closeModal(){
    //get the modal tag
    $("#the-modal").remove();

}
function addComment() {
    // When the user adds comment, make a POST request
}

function goBackToTop() {
    // A "Back to Top" button will be displayed on the homepage.
    // When the user scrolls far down and clicks on the button, they should go to the top of the page.
    //WHICH JS COMMAND WORKS!
    window.scrollTo(0,0);
    console.log("back to top");
}

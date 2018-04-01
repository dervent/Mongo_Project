/**
 * Client-Side JavaScript
 */
var BASE_URL = 'http://127.0.0.1:5000';

function searchForDocs() {
    // Get text from search bar
    var jsonObj = new Object();
    jsonObj.text = document.getElementById("searchBar").value;

    var filterVal = $('input[name=filters]:checked').val();
    var sortVal = $('input[name=sorts]:checked').val();

    if(typeof filterVal != 'undefined') jsonObj.filter = filterVal;
    if(typeof sortVal != 'undefined') jsonObj.sort = sortVal;

    var qurl = BASE_URL + '/search';

    $.ajax(
        {
            url:qurl,
            type:"GET",
            async:true,
            data:jsonObj,
            success:function(result){
                $('#results')[0].innerHTML = result;
            }
        }
    );
}

function openDetailsModal(object_id){
    var jsonObj = new Object();
    jsonObj.id = object_id;
    var qurl = BASE_URL + '/details';
    $.ajax(
        {
            url:qurl,
            type:"GET",
            async:true,
            data:jsonObj,
            success:function(result){
                $('#detailsBody')[0].innerHTML = result;
                $('#submit-comment-button').detach().insertAfter('#comment-box');
                $('#the-modal').css({'display': 'block'})
            }
        }
    );
}

function closeModal(){
    $("#the-modal").css({'display' : 'none'});
    $("#detailsBody").empty();
    $("#submit-comment-button").remove();
}

function addComment(object_id) {
    // When the user adds comment, make a POST request
    var jsonObj = new Object();
    jsonObj.text = $('#comment-field')[0].value;
    jsonObj.id = object_id;
    var qurl = BASE_URL + '/comment';

    $.ajax(
        {
            url:qurl,
            type:"POST",
            async:true,
            data:jsonObj,
            success:function(){
                // TODO: Clear the comment field and display a message below it in green, 'Comment successfully posted!'
                console.log("comment posted");
            }
        }
    );
}

function goBackToTop() {
    // A "Back to Top" button will be displayed on the homepage.
    // When the user scrolls far down and clicks on the button, they should go to the top of the page.
    //WHICH JS COMMAND WORKS!
    window.scrollTo(0,0);
    console.log("back to top");
}

// Localhost URL and port number used by application.
var BASE_URL = 'http://127.0.0.1:5000';

function searchForDocs() {
    var jsonObj = new Object();

    // Get text from search bar.
    jsonObj.text = document.getElementById("searchBar").value;

    // Get values of selected radio buttons.
    var filterVal = $('input[name=filters]:checked').val();
    var sortVal = $('input[name=sorts]:checked').val();

    if(typeof filterVal != 'undefined') jsonObj.filter = filterVal;
    if(typeof sortVal != 'undefined') jsonObj.sort = sortVal;

    var qurl = BASE_URL + '/search';

    // Make AJAX GET request to server to get list of names/titles.
    $.ajax(
        {
            url:qurl,
            type:"GET",
            async:true,
            data:jsonObj,
            success:function(result){
                // Response with document names/titles is displayed to user.
                $('#results')[0].innerHTML = result;
            }
        }
    );
}

function openDetailsModal(object_id){
    var jsonObj = new Object();
    jsonObj.id = object_id;
    var qurl = BASE_URL + '/details';

    // Make AJAX GET request to server to get details for a document.
    $.ajax(
        {
            url:qurl,
            type:"GET",
            async:true,
            data:jsonObj,
            success:function(result){
                // Display modal with details for selected title.
                $('#detailsBody')[0].innerHTML = result;
                $('#submit-comment-button').detach().insertAfter('#comment-box');
                $('#the-modal').css({'display': 'block'})
            }
        }
    );
}

function closeModal(){
    // Hide modal and dispose of document details.
    $("#the-modal").css({'display' : 'none'});
    $("#detailsBody").empty();
    $("#submit-comment-button").remove();
    $(".comment-confirm").remove();
}

function addComment(object_id) {
    var jsonObj = new Object();

    // Get user string from comment textbox.
    jsonObj.text = $('#comment-field')[0].value;
    jsonObj.id = object_id;
    var qurl = BASE_URL + '/comment';

    // Make AJAX POST request to server add comment to document.
    $.ajax(
        {
            url:qurl,
            type:"POST",
            async:true,
            data:jsonObj,
            success:function(){
                $("#comment-field").val('');
                $("#comment-box").append("<p class='comment-confirm' style='color: #2e7d32'><strong>" +
                    "Comment successfully posted!</strong></p>");
            },
            error:function() {
                 $("#comment-box").append("<p class='comment-fail' style='color: #8B0000'><strong>" +
                    "Unable to post your comment Please try another time.</strong></p>");
            }
        }
    );
}

function goBackToTop() {
    // Scrolls back to the top of the page.
    $(".mdl-layout__content").animate({scrollTop:0});
}

function clearTextAndSelections(){
    // Clear radio button selections and remove text from search bar.
    $(".mdl-radio").removeClass("is-checked");
    $("#searchBar").val("");

}

function clearCommentMessage() {
    // Clear comment message, if present.
    if($(".comment-confirm").length) {
        $(".comment-confirm").remove();
    }
    else if($(".comment-fail").length) {
        $(".comment-fail").remove();
    }
}

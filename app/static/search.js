/**
 * Client-Side JavaScript
 */
var BASE_URL = 'http://127.0.0.1:5000';
//This runs to stop menus from closing on first click

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
    $(".comment-confirm").remove();
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
    // A "Back to Top" button will be displayed on the homepage.
    // When the user scrolls far down and clicks on the button, they should go to the top of the page.
    $(".mdl-layout__content").animate({scrollTop:0});
}

function clearSelectedRadioButtons(){
    //make the button to call this
    //also check to make sure dropdowns stay down
    console.log("Clearing that shit");
    $(".mdl-radio").removeClass("is-checked");

}

function clearCommentConfirm() {
    if($(".comment-confirm").length) {
        $(".comment-confirm").remove();
    }
    else if($(".comment-fail").length) {
        $(".comment-fail").remove();
    }
}

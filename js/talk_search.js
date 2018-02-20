const MongoClient = require('mongodb').MongoClient;

MongoClient.connect('mongodb://localhost:27017/TedTalks', (err, client) => {
    db = client.db("TedTalks");
    var collection = db.collection('Talks');
    console.log(collection);
  // ... do something here
});

//output = $('#DBoutput');
//
// document.querySelector('.mdl-menu').addEventListener('click', function(event) {
//   event.stopPropagation();
// });
//
function SearchTest(ele){
    //TODO:Eventually it will connect to the DB. Connect and close at the end of each function
    //output.empty();
    //output.append(ele.value)
    fields = checkfields();
    console.log(fields);
}
// //output.empty();
//
// // function SearchReturnField(field, value){
// //     //TODO: Field should be a list. Not sure how hard that will be to convert.
// //     //main search regex (for now)
// //     cursor = collection.find({[field]: {$regex: new RegExp(".*"+value+".*","i")}},{[field]:1,_id:0});
// //     //TODO: instead of just printing here it will send it to an element on the page.
// //     while (cursor.hasNext()) {
// //         printjson(cursor.next());
// //     }
// // }
// //
// // function SearchReturnAll(value){
// //     fields = checkFields();
// //     //TODO: Field should be a list. Not sure how hard that will be to convert. Gonna need to use an $or
// //     //main search regex (for now)
// //     cursor = collection.find({[field]: {$regex: new RegExp(".*"+value+".*","i")}},{_id:0});
// //     //TODO: instead of just printing here it will send it to an element on the page.
// //     while (cursor.hasNext()) {
// //         printjson(cursor.next());
// //     }
// // }
//
//
function checkfields(){
    fields = new Array();
    $(":checkbox").each(function(n,ele){
        //for each check box
        if (ele.checked){
            /*
            * All elements are named the same- fieldname_Check
            * This adds the name of the field to the fields array by splitting it.
            * fieldname_Check.split('_')[0] -> ['fieldname','Check'] [0] -> fieldname
            */
            fields.push(ele.id.split("_")[0]);
        }
    });
    return fields;
}
// checkfields();
// //This data will be populated by some form of user input when it is called
// //TODO: Make entire gui...lol
// //SearchReturnAll("name","john");
// //Search("description","computer");

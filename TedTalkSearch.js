//connect to the local Mongo Instance
connection = new Mongo("localhost:27017");
//choose which database in the running Mongo Instance
db = connection.getDB("TedTalks");
//choose which collection in the database
collection = db.getCollection('TalkData');

function Search(field, value){
    //TODO: Field should be a list. Not sure how hard that will be to convert.
    //main search regex (for now)
    cursor = collection.find({[field]: {$regex: new RegExp(".*"+value+".*","i")}},{[field]:1,_id:0});
    //TODO: instead of just printing here it will send it to an element on the page.
    while (cursor.hasNext()) {
        printjson(cursor.next());
    }
}

//This data will be populated by some form of user input when it is called
//TODO: Make entire gui...lol
Search("name","ross");
//Search("description","computer");

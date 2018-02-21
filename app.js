//connect to the local Mongo Instance
//const connection = new Mongo("localhost:27017");
//choose which database in the running Mongo Instance
//db = connection.getDB("TedTalks");
//choose which collection in the database
//collection = db.getCollection('TalkData');
const express = require('express');
const app = express();
app.use(express.static('pages'));
app.use(express.static('css'));
app.use(express.static('js'));
//app.use(express.static('../SiteFiles'));

var PORT = 3000;
app.listen(PORT,function(){
    console.log("listening on port:" + PORT);
});

// app.get('/', function(req, res) {
//   res.sendFile(__dirname + '/index.html');
//   console.log(req);
//
// })
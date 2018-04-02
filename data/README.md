# Database

## Loading Data Set
The data set for the database was obtained from [Ted Data Analysis](https://www.kaggle.com/rounakbanik/ted-data-analysis/data) on Kaggle.
This data was then pruned to suit the needs of this project. 
Use the command to load the CSV data set (found inside `\ted_talks_dataset` directory) into a local instance of your database: <br/>
`mongoimport --db TedTalks --collection Talks --type csv --file <your_local_path>\ted_main.csv --headerline`

## Data Transformation
Run the _transform_data.py_ to transform the remaining data in the Talks collection. Your database instance should be running.

## Loading Images
The main speakers for the first five documents in the TedTalks database were obtained from around the web. These images capture the speaker doing the actual Ted Talk.
 
 Use the GridFS commands to add each image (you may Google your own) to the database: <br/>
```
mongofiles --db TedTalks put AlGore.jpg --local <your_local_path>\AlGore.jpg

mongofiles --db TedTalks put DavidPogue.jpg --local C<your_local_path>\DavidPogue.jpg

mongofiles --db TedTalks put HansRosling.jpg --local <your_local_path>\HansRosling.jpg

mongofiles --db TedTalks put KenRobinson.jpg --local <your_local_path>KenRobinson.jpg

mongofiles --db TedTalks put MajoraCarter.jpg --local <your_local_path>\MajoraCarter.jpg
```

## Referencing Images from Documents
A 1:1 relationship model was used to reference an image from the `fs.files` collection within a document. 

The image ids were added to the matching documents using the following commands: <br/>
```
// Speaker: Al Gore
db.Talks.update({_id:ObjectId("5ab6e91ad9cc6aee3e8247e2")}, {$set: {image_id: ObjectId("5a8e365b8334de05708f0027")}})

// Speaker: Ken Robinson
db.Talks.update({_id:ObjectId("5ab6e91ad9cc6aee3e8247e3")}, {$set: {image_id: ObjectId("5a8e36ae8334de1eb873d3df")}})

// Speaker: David Pogue
db.Talks.update({_id:ObjectId("5ab6e91ad9cc6aee3e8247e4")}, {$set: {image_id: ObjectId("5a8e36678334de0e645057bb")}})

// Speaker: Majora Carter
db.Talks.update({_id:ObjectId("5ab6e91ad9cc6aee3e8247e5")}, {$set: {image_id: ObjectId("5a8e36cb8334de0ac4642c76")}})

// Speaker: Hans Rosling
db.Talks.update({_id:ObjectId("5ab6e91ad9cc6aee3e8247e6")}, {$set: {image_id: ObjectId("5a8e367d8334de0c20b63c91")}})
```

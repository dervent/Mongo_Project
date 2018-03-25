from pymongo import MongoClient
import ast

# This file transforms several fields from their raw formats to other formats
# that are suitable for storage in the Talks collection

client = MongoClient('localhost', 27017)
database = client.TedTalks
collection = database.Talks

cursor = collection.find()
for doc in cursor:
    # add 'comments' field with empty array values
    collection.update_one({'_id': doc['_id']}, {'$set': {'comments': []}})

    # reformat each 'tags' field value to an array of strings
    arrayString = doc['tags']
    tagsArray = ast.literal_eval(arrayString)
    collection.update_one({'_id': doc['_id']}, {'$set': {'tags': tagsArray}})

    # reformat each 'ratings' field value to an array of sub-documents
    arrayString = doc['ratings']
    ratingsArray = ast.literal_eval(arrayString)
    collection.update_one({'_id': doc['_id']}, {'$set': {'ratings': ratingsArray}})

    # reformat each 'related_talks' field value to an array of sub-documents
    arrayString = doc['related_talks']
    ratingsArray = ast.literal_eval(arrayString)
    collection.update_one({'_id': doc['_id']}, {'$set': {'related_talks': ratingsArray}})

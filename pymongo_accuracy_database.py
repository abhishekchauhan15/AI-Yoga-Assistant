from pymongo import MongoClient
client=MongoClient("mongodb+srv://test:test@cluster0.8bxh1lq.mongodb.net/?retryWrites=true&w=majority")
db=client.get_database('Yoga_Data')
records=db.Accuracy_data
#count the documents
from app import(accArray)
records.count_documents({})

#insert the document

new_acc = {"name": 'kanika',
  "data":{
     'accuracy':45,
     'duration':15,
     
 }
 } 



records.insert_one(new_acc)


new_acc_1 = {"name": 'abhishek',
  "data":{
     'accuracy':25,
     'duration':10,
     
 }
 } 



records.insert_one(new_acc_1)

new_acc_2 = {"name": 'jaideep',
  "data":{
     'accuracy':95,
     'duration':35,
     
 }
 } 



records.insert_one(new_acc_2)


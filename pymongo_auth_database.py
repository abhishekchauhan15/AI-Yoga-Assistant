from pymongo import MongoClient
client=MongoClient("mongodb+srv://test:test@cluster0.8bxh1lq.mongodb.net/?retryWrites=true&w=majority")
db=client.get_database('Yoga_Data')
records=db.Auth_data
#count the documents

#insert the document
new_acc_auth = {
    'name': 'Kanika',
    'email':'kanikagola26@gmail.com',
    'password':'hsdbj',
}

records.insert_one(new_acc_auth)

new_acc_auth_1 = {
    'name': 'Abhishek',
    'email':'abhisheksingh26@gmail.com',
    'password':'shfd',
}

records.insert_one(new_acc_auth_1)

new_acc_auth_2 = {
    'name': 'Jaideep',
    'email':'jaideepsolania26@gmail.com',
    'password':'dgvejfuh',
}

records.insert_one(new_acc_auth_2)
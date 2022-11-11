# // how to connect mongodb with python?
from pymongo import MongoClient
client = MongoClient('localhost:27017')

def my_function(mydb):
    db = client.get_database(mydb)
    return db.collection.find().count()

print(my_function('my_database'))



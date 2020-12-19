
import pymongo
from pymongo import MongoClient
from bson.objectid import ObjectId

class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """
    def __init__(self, username, password):
        # Initializing the MongoClient. This helps to 
        # access the MongoDB databases and collections. 
        try:
            self.client = MongoClient('mongodb://%s:%s@localhost:32574' % (username, password))
            self.database = self.client['AAC']
            self.collection = self.database['animals']
            return print('Connected')
        except Exception as e:
            return print('Could not connect')
            raise e
        

# Complete this create method to implement the C in CRUD.
    def create(self, data):
        if data is not None:
            self.collection.insert(data)# data should be dictionary           
        else:
            raise Exception("Nothing to save, because data parameter is empty")

    def read(self, data):
        if data is not None:
            return self.collection.find(data,{"_id":False})
        else:
            print('Nothing to read, because data parameter is empty')
            return False

        
    def update(self,data, dataToUpdate):
        try:
            result = self.collection.update_one(data, dataToUpdate)
            print(result)
            print('updated')
        except Exception as e:
            print ("Could not find entry")
            return e   
        
    def delete(self, data):
        if data is not None:
            return self.database.animals.delete_one(data) # data is dictionary
        else:
            print('Nothing to delete, because data parameter is empty')
            return False
    
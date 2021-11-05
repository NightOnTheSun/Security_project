import pymongo 
import datetime
import time



class mongodb_atlas_test:
    def __init__(self):
        """
        TODO: This client connection string needs to probabaly be secured. Need to figure out what 
        the best way to do this is.
        """
        self.client = pymongo.MongoClient('TEST')
        self.db = self.client.myFirstDatabase
        self.collection = self.db.user_info

    def insert_data(self,data):
        """
        This function is used to insert data into the database collection.
        @param data: This is the data that is to be inserted into the database. Dictionary format.
        """
        self.collection.insert_one(data)
    def get_data(self,data):
        """
        This function is used to get data from the database collection.
        @param data: This is the data that is to be inserted into the database. Dictionary format.
        """
        self.collection.find_one(data)
    def delete_data(self,data):
        """
        This function is used to delete data from the database collection.
        @param data: This is the data that is to be inserted into the database. Dictionary format.
        """
        self.collection.delete_one(data)
    def get_all_data(self):
        """
        This function is used to get all data from the database collection.
        """
        self.collection.find()
    def upsert_data(self,data):
        """
        This function is used to upsert data into the database collection.
        @param data: This is the data that is to be inserted into the database. Dictionary format.
        """
        self.collection.update_one(data,{'$set':data},upsert=True)
    

if __name__ == "__main__":
    mongodb_atlas_test = mongodb_atlas_test()
    data = {
        "name": "John",
        "address": "Highway 37",
        "phone": "555-5555"
    }

    mongodb_atlas_test.insert_data(data)
    mongodb_atlas_test.get_all_data()
    
    
    
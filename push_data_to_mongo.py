import sys
import pandas as pd
import pymongo
import json
from fake_news_classification.exception.exception import NewsException

class PushDataMongodb():
    def __init__(self):
        try:
            conn = pymongo.MongoClient(host='localhost', port=27017)
            print("Successfully conned to mongodb.")
        except Exception as e:
            raise NewsException(e, sys)
    
    def convert_csv_to_json(self, file_path):
        try:
            df = pd.read_csv(file_path)
            df.reset_index(drop=True, inplace=True)
            data_records = list(json.loads(df.T.to_json()).values())
            
            return data_records
        except Exception as e:
            raise NewsException(e, sys)
    
    def push_data_to_mongodb(self, data_records, database, collection, host='localhost', port=27017):
        try:
            self.database = database
            self.collection = collection
            self.data_records = data_records
            
            self.client = pymongo.MongoClient(host=host, port=port)
            
            self.database = self.client[self.database]
            self.collection = self.database[self.collection]
            self.collection.insert_many(self.data_records)
            return len(self.data_records)
        except Exception as e:
            raise NewsException(e, sys)
    

if __name__ == "__main__":
    FILE_PATH = "notebooks\Datasets\WELFake_Dataset.csv"
    DATABASE = "news_db"
    COLLECTION = "news"
    
    push_data = PushDataMongodb()
    data_records = push_data.convert_csv_to_json(FILE_PATH)
    num_of_records = push_data.push_data_to_mongodb(data_records=data_records, database=DATABASE, collection=COLLECTION)
    print(num_of_records)
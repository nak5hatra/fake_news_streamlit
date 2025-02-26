import sys
import os
import pymongo
import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split

from fake_news_classification.exception.exception import NewsException
from fake_news_classification.entity.config_entity import DataIngestionConfig
from fake_news_classification.entity.artifact_entity import DataIngestionArtifact

class DataIngestion:
    def __init__(self, data_ingestion_config:DataIngestionConfig):
        try:
            self.data_ingestion_config = data_ingestion_config
        except Exception as e:
            raise NewsException(e, sys)
        
    def get_data_from_database(self):
        try:
            database_name = self.data_ingestion_config.database_name
            collection_name = self.data_ingestion_config.collection_name
            database_host = self.data_ingestion_config.database_host
            database_port = self.data_ingestion_config.database_port
            self.client = pymongo.MongoClient(host=database_host, port=database_port)
            collections = self.client[database_name][collection_name]
            df = pd.DataFrame(list(collections.find()))
            
            df.drop(columns=['_id', 'Unnamed: 0'], inplace=True)
            df.fillna(' ', inplace=True)
            return df
        
        except Exception as e:
            raise NewsException(e, sys)
    
    def export_data_to_feature_store(self, dataframe: pd.DataFrame):
        try:
            feature_store_file_path = self.data_ingestion_config.feature_store_path
            
            dir_path = os.path.dirname(feature_store_file_path)
            os.makedirs(dir_path, exist_ok=True)
            dataframe.to_csv(feature_store_file_path, index=False, header=True)
            return dataframe
        except Exception as e:
            raise NewsException(e, sys)
        
    def split_data_to_train_test_sets(self, dataframe: pd.DataFrame):
        try:
            train_test_split_ratio = self.data_ingestion_config.train_test_split_ratio
            
            train_data_set, test_data_set = train_test_split(
                dataframe,
                test_size=train_test_split_ratio,
                random_state=42
            )
            
            ## saving train set
            dir_path = os.path.dirname(self.data_ingestion_config.train_file_path)
            os.makedirs(dir_path, exist_ok=True)
            train_data_set.to_csv(self.data_ingestion_config.train_file_path, index=False, header=True)
            
            ## saving test set
            dir_path = os.path.dirname(self.data_ingestion_config.test_file_path)
            os.makedirs(dir_path, exist_ok=True)
            test_data_set.to_csv(self.data_ingestion_config.test_file_path, index=False, header=True)
            
        except Exception as e:
            raise NewsException(e, sys)
    
    def start_data_ingestion(self):
        try:
            dataframe = self.get_data_from_database()
            dataframe = self.export_data_to_feature_store(dataframe=dataframe)
            self.split_data_to_train_test_sets(dataframe=dataframe)
            data_ingestion_artifact_paths = DataIngestionArtifact(
                train_file_path=self.data_ingestion_config.train_file_path,
                test_file_path=self.data_ingestion_config.test_file_path
            ) 
            return data_ingestion_artifact_paths
        except Exception as e:
            raise NewsException(e, sys)
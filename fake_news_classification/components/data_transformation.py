import pandas as pd
import numpy as np
import sys
import nltk
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer
from fake_news_classification.exception.exception import NewsException
from fake_news_classification.entity.config_entity import DataTransformationConfig
from fake_news_classification.entity.artifact_entity import DataTransformationArtifact, DataIngestionArtifact
from utils.main_urils.utils import read_data, save_npy, save_npz, save_models
nltk.download('stopwords')
stop = stopwords.words('english')

class DataTransformation:
    def __init__(
        self, 
        data_ingestion_artifact: DataIngestionArtifact,
        data_transformation_config: DataTransformationConfig
    ):
        try:
            self.data_ingestion_artifact = data_ingestion_artifact
            self.data_transformation_config = data_transformation_config
        except Exception as e:
            raise NewsException(e, sys)
    
    def initiate_data_transformation(self) -> DataTransformationArtifact:
        try:
            train_df = read_data(self.data_ingestion_artifact.train_file_path)
            test_df = read_data(self.data_ingestion_artifact.test_file_path)
            train_df['title'] = train_df['title'].apply(lambda x:x.lower())
            
            pattern = r'[^\w\s]'
            train_df['title'] = train_df['title'].replace(pattern, '', regex=True)
            
            ## training dataframe
            train_inupt_feature = train_df['title'].values
            train_target_feature = train_df['label']
            
            ## testing dataframe
            test_input_feature = test_df['title'].values
            test_target_feature = test_df['label']
            
            preprocessor = TfidfVectorizer(lowercase=False)
            train_inupt_feature = preprocessor.fit(train_inupt_feature)
            test_input_feature = preprocessor.transform(test_input_feature)
            
            
            ## saving train_inupt_feature, train_target_feature, test_input_feature, test_target_feature
            save_npz(self.data_transformation_config.x_train_file_path, train_inupt_feature)
            save_npz(self.data_transformation_config.x_test_file_path, test_input_feature)
            
            save_npy(self.data_transformation_config.y_train_file_path, train_target_feature)
            save_npy(self.data_transformation_config.y_test_file_path, test_target_feature)
            
            ## saving preprocessor
            save_models(self.data_transformation_config.preprocessor_file_path, preprocessor)
            
            data_transformation_artifact =DataTransformationArtifact(
                x_train_file_path=self.data_transformation_config.x_train_file_path,
                x_test_file_path=self.data_transformation_config.x_test_file_path,
                y_test_file_path=self.data_transformation_config.y_test_file_path,
                y_train_file_path=self.data_transformation_config.y_train_file_path,
                preprocessor_file_path= self.data_transformation_config.preprocessor_file_path
            )
            
            return data_transformation_artifact
            
        except Exception as e:
            raise NewsException(e, sys)
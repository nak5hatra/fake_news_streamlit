import sys
import os
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.feature_extraction.text import TfidfVectorizer

from fake_news_classification.entity.artifact_entity import DataTransformationArtifact, ModelTrainerArtifact
from fake_news_classification.exception.exception import NewsException
from fake_news_classification.entity.config_entity import ModelTrainerConfig
from utils.main_urils.utils import save_models, evaluate_model, load_files

class ModelTrainer:
    def __init__(self, data_transformation_artifact: DataTransformationArtifact, model_trainer_config: ModelTrainerConfig):
        try:
            self.model_trainer_config = model_trainer_config
            self.data_transformation_artifact = data_transformation_artifact
        except Exception as e:
            raise NewsException(e, sys)
        
    def model_trainer(self, X_train, y_train, X_test, y_test):
        try:
            ## in my notebook i found out that Random Forest and logistic Regression perfomed well so i'm using only Random Forest
            
            preprocessor = TfidfVectorizer()
            X_train = preprocessor.fit_transform(X_train)
            X_test = preprocessor.transform(X_test)
            
            ## saving preprocessor 
            save_models(self.model_trainer_config.model_preprocessor_file_path, model=preprocessor)
            
            model = RandomForestClassifier(verbose=1)
            model.fit(X_train, y_train)
            y_pred = model.predict(X_test)
            
            model_score = evaluate_model(y_true=y_test, y_pred=y_pred)
            save_models(self.model_trainer_config.model_file_name, model=model)
            
            model_trainer_artifact = ModelTrainerArtifact(
                model_file_path=self.model_trainer_config.model_file_name,
                preprocessor_file_path=self.model_trainer_config.model_preprocessor_file_path
            )
            return model_trainer_artifact
        except Exception as e:
            raise NewsException(e, sys)
        
    def inititate_model_training(self):
        try:
           X_train = load_files(self.data_transformation_artifact.x_train_file_path)
           X_test = load_files(self.data_transformation_artifact.x_test_file_path)
           y_train = load_files(self.data_transformation_artifact.y_train_file_path)
           y_test = load_files(self.data_transformation_artifact.y_test_file_path)
           model_trainer_artifact = self.model_trainer(X_train, y_train, X_test, y_test)
           return model_trainer_artifact
        except Exception as e:
            raise NewsException(e, sys)
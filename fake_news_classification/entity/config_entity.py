import os
from datetime import datetime
from fake_news_classification.constants import training_pipeline

class TrainingPipelineConfig:
    def __init__(self, timestamp = datetime.now()):
        timestamp = timestamp.strftime("%m_%d_%Y_%M_%S")
        self.pipelie_name: str = training_pipeline.PIPELINE_NAME
        self.artifact_name: str = training_pipeline.ARTIFACT_DIR
        self.artifact_dir: str = os.path.join(self.artifact_name, timestamp)
        self.timestamp: str = timestamp
        

class DataIngestionConfig:
    def __init__(self,training_pipeline_config:TrainingPipelineConfig):
        self.data_validation_dir: str = os.path.join(
            training_pipeline_config.artifact_dir,
            training_pipeline.DATA_INGESTION_DIR_NAME
        )
        
        self.feature_store_path: str = os.path.join(
            self.data_validation_dir, training_pipeline.DATA_INGESTION_FEATURE_STORE_DIR, training_pipeline.FILE_NAME
        )
        
        self.train_file_path: str = os.path.join(
            self.data_validation_dir, training_pipeline.DATA_INGESTION_INGESTED_DIR, training_pipeline.TRAIN_FILE_NAME
        )
        
        self.test_file_path: str = os.path.join(
            self.data_validation_dir, training_pipeline.DATA_INGESTION_INGESTED_DIR, training_pipeline.TEST_FILE_NAME
        )
        
        self.train_test_split_ratio: float = training_pipeline.DATA_INGESTION_TRAIN_TEST_SPLIT
        self.collection_name: str = training_pipeline.DATA_INGESTION_COLLECTION_NAME
        self.database_name: str = training_pipeline.DATA_INGESTION_DATABASE_NAME
        self.database_host: str = training_pipeline.DATA_INGESTION_DATABASE_HOST
        self.database_port: int = training_pipeline.DATA_INGESTION_DATABASE_PORT

class DataTransformationConfig:
    def __init__(self, training_pipeline_config: TrainingPipelineConfig):
        self.data_transformation_dir: str = os.path.join(
            training_pipeline_config.artifact_dir, 
            training_pipeline.DATA_TRANFORMATION_DIR_NAME
        )
        
        self.x_train_file_path: str = os.path.join(
            self.data_transformation_dir, training_pipeline.DATA_TRANFORMATION_FEATURE_STORE_DIR, training_pipeline.DATA_TRANFORMATION_X_TRAIN_FILE_NAME
        )
        self.x_test_file_path: str = os.path.join(
            self.data_transformation_dir, training_pipeline.DATA_TRANFORMATION_FEATURE_STORE_DIR, training_pipeline.DATA_TRANFORMATION_X_TEST_FILE_NAME
        )
        self.y_train_file_path: str = os.path.join(
            self.data_transformation_dir, training_pipeline.DATA_TRANFORMATION_FEATURE_STORE_DIR, training_pipeline.DATA_TRANFORMATION_Y_TRAIN_FILE_NAME
        )
        self.y_test_file_path: str = os.path.join(
            self.data_transformation_dir, training_pipeline.DATA_TRANFORMATION_FEATURE_STORE_DIR, training_pipeline.DATA_TRANFORMATION_Y_TEST_FILE_NAME
        )

class ModelTrainerConfig:
    def __init__(self, training_pipeline_config: TrainingPipelineConfig):
        self.model_trainer_dir: str = os.path.join(
            training_pipeline_config.artifact_dir, 
            training_pipeline.MODEL_TRAINER_DIR_NAME
        )
        
        self.model_file_name: str = os.path.join(
            self.model_trainer_dir, training_pipeline.MODEL_TRAINER_TRAINED_MODEL_DIR, training_pipeline.MODEL_TRAINER_TRAINED_MODEL_NAME
        )
        
        self.model_preprocessor_file_path: str = os.path.join(
            self.model_trainer_dir, training_pipeline.DATA_TRAINER_PREPROCESSOR_OBJECT_DIR, training_pipeline.PREPROCESSOR_FILE_NAME
        )
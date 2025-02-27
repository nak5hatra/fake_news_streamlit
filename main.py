import sys
from fake_news_classification.components.data_ingestion import DataIngestion
from fake_news_classification.exception.exception import NewsException
from fake_news_classification.components.data_transformation import DataTransformation
from fake_news_classification.components.model_trainer import ModelTrainer
from fake_news_classification.entity.config_entity import DataIngestionConfig, TrainingPipelineConfig, DataTransformationConfig, ModelTrainerConfig



if __name__ == "__main__":
    try:
        traning_pipeline_config = TrainingPipelineConfig()
        data_ingestion_config = DataIngestionConfig(training_pipeline_config=traning_pipeline_config)
        data_ingestion = DataIngestion(data_ingestion_config=data_ingestion_config)
        data_ingestion_artifact = data_ingestion.start_data_ingestion()

        print(data_ingestion_artifact)

        data_transformation_config = DataTransformationConfig(training_pipeline_config=traning_pipeline_config)
        data_transformation = DataTransformation(data_ingestion_artifact=data_ingestion_artifact, data_transformation_config=data_transformation_config)
        data_transformation_artifact = data_transformation.initiate_data_transformation()
        print(data_transformation_artifact)

        model_trainer_config = ModelTrainerConfig(training_pipeline_config=traning_pipeline_config)
        model_trainer = ModelTrainer(data_transformation_artifact=data_transformation_artifact, model_trainer_config=model_trainer_config)
        model_trainer_artifact = model_trainer.inititate_model_training()
        print(model_trainer_artifact)
    except Exception as e:
        raise NewsException(e, sys)
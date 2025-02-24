from fake_news_classification.components.data_ingestion import DataIngestion
from fake_news_classification.entity.config_entity import DataIngestionConfig, TrainingPipelineConfig



traning_pipeline_config = TrainingPipelineConfig()
data_ingestion_config = DataIngestionConfig(training_pipeline_config=traning_pipeline_config)
data_ingestion = DataIngestion(data_ingestion_config=data_ingestion_config)
    
data = data_ingestion.start_data_ingestion()
print(data)
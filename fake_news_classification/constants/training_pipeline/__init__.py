"""
Common constents are defined below..
"""

PIPELINE_NAME: str = "FakeNews"
ARTIFACT_DIR: str = "Artifacts"
FILE_NAME: str = "WELFake_Dataset.csv"

TRAIN_FILE_NAME: str = "train.csv"
TEST_FILE_NAME: str = "test.csv"
PREPROCESSOR_FILE_NAME: str = "preprocessor.pkl"


"""
Data Ingestion Constants : DATA_INGESTION_xx 
"""

DATA_INGESTION_COLLECTION_NAME: str = "news"
DATA_INGESTION_DATABASE_NAME: str ="news_db"
DATA_INGESTION_DIR_NAME: str = "Data_ingestion"
DATA_INGESTION_FEATURE_STORE_DIR: str = "feature_store"
DATA_INGESTION_INGESTED_DIR: str ="ingested"
DATA_INGESTION_TRAIN_TEST_SPLIT: float = 0.2
DATA_INGESTION_DATABASE_HOST: str = "localhost"
DATA_INGESTION_DATABASE_PORT: int = 27017


"""
Data Transformation Constants : DATA_TRANFORMATION_xx 
"""

DATA_TRANFORMATION_DIR_NAME: str = "Data_Tranformation"
DATA_TRANFORMATION_FEATURE_STORE_DIR: str = "feature_store"
DATA_TRANFORMATION_TRANSFORMED_DIR: str = "transfomed"
DATA_TRANFORMATION_X_TRAIN_FILE_NAME: str = 'x_train.npy'
DATA_TRANFORMATION_X_TEST_FILE_NAME: str = 'x_test.npy'
DATA_TRANFORMATION_Y_TRAIN_FILE_NAME: str = 'y_train.npy'
DATA_TRANFORMATION_Y_TEST_FILE_NAME: str = 'y_test.npy'



"""
Model Trainer Constants : MODEL_TRAINER_xx
"""

MODEL_TRAINER_DIR_NAME: str = "model_trainer"
MODEL_TRAINER_TRAINED_MODEL_DIR: str = "trained_model"
MODEL_TRAINER_TRAINED_MODEL_NAME: str = "model.pkl"
DATA_TRAINER_PREPROCESSOR_OBJECT_DIR: str = "transformed_object"
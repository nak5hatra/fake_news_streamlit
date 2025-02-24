"""
Common constents are defined below..
"""

PIPELINE_NAME: str = "FakeNews"
ARTIFACT_DIR: str = "Artifacts"
FILE_NAME: str = "WELFake_Dataset.csv"

TRAIN_FILE_NAME: str = "train.csv"
TEST_FILE_NAME: str = "test.csv"


"""
Data ingestion Constants : DATA_INGESTION_xx 
"""

DATA_INGESTION_COLLECTION_NAME: str = "news"
DATA_INGESTION_DATABASE_NAME: str ="news_db"
DATA_INGESTION_DIR_NAME: str = "Data_ingestion"
DATA_INGESTION_FEATURE_STORE_DIR: str = "feature_store"
DATA_INGESTION_INGESTED_DIR: str ="ingested"
DATA_INGESTION_TRAIN_TEST_SPLIT: float = 0.2
DATA_INGESTION_DATABASE_HOST: str = "localhost"
DATA_INGESTION_DATABASE_PORT: int = 27017

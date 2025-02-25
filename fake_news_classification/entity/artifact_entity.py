from dataclasses import dataclass

@dataclass
class DataIngestionArtifact:
    train_file_path: str
    test_file_path: str


@dataclass
class DataTransformationArtifact:
    x_train_file_path: str
    x_test_file_path: str
    y_train_file_path: str
    y_test_file_path: str
    preprocessor_file_path: str
    
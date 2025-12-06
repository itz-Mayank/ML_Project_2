from dataclasses import dataclass
#It is a decorator which writes cleaner code to store the data in good form by automatically creating the boilerplate like __init__, or any functions.

@dataclass
class DataIngestionArtifacts:
    # feature_store_file_path: str
    train_file_path: str
    test_file_path: str

@dataclass
class DataValidationArtifacts:
    validation_status: bool
    valid_train_file_path: str
    valid_test_file_path: str
    invalid_train_file_path: str
    invalid_test_file_path: str
    drift_report_file_path: str
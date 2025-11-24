from dataclasses import dataclass 
#It is a decorator which writes cleaner code to store the data in good form by automatically creating the boilerplate like __init__, or any functions.

@dataclass
class DataIngestionArtifacts:
    # feature_store_file_path: str
    train_file_path: str
    test_file_path: str
from dataclasses import dataclass
import pandas as pd
import os

@dataclass
class DataIngestionConfig:
    training_data_path = os.path.join("artifacts\\train.csv")
    testing_data_path = os.path.join("artifacts\\test.csv")

class DataIngestion:
    def __init__(self):
        self.data_ingestion_config = DataIngestionConfig()

    def initiate_data_ingestion(self):
        train_df = pd.read_csv("notebook\\data\\train.csv")
        test_df = pd.read_csv("notebook\\data\\test.csv")

        os.makedirs("artifacts", exist_ok=True)

        train_df.to_csv(self.data_ingestion_config.training_data_path)
        test_df.to_csv(self.data_ingestion_config.testing_data_path)

        return train_df,test_df

if __name__ == '__main__':
    data_ingestion = DataIngestion()
    train_df, test_df = data_ingestion.initiate_data_ingestion()
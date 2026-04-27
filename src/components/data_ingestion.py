from dataclasses import dataclass
import pandas as pd
import os
from src.logger import logging
from src.components.data_transformation import DataTransformation
from src.components.model_trainer import ModelTrainer
from sklearn.model_selection import train_test_split
from src.exception import CustomException
import sys

@dataclass
class DataIngestionConfig:
    training_data_path = os.path.join("artifacts\\train.csv")
    testing_data_path = os.path.join("artifacts\\test.csv")

class DataIngestion:
    def __init__(self):
        self.data_ingestion_config = DataIngestionConfig()

    def initiate_data_ingestion(self):
        try:
            raw_df = pd.read_csv("notebook\\data\\raw.csv")

            os.makedirs("artifacts", exist_ok=True)

            num_df = raw_df.select_dtypes(exclude="object")

            Q1 = num_df.quantile(0.25)
            Q3 = num_df.quantile(0.75)
            IQR = Q3 - Q1

            lower = Q1 - 1.5 * IQR
            upper = Q3 + 1.5 * IQR

            outlier_rows = num_df[((num_df < lower) | (num_df > upper)).any(axis=1)]

            raw_df.drop(outlier_rows.index, axis = 0,inplace=True)

            raw_df = raw_df.dropna(subset=['MasVnrArea', 'Electrical', 'BsmtExposure'])

            raw_df.drop(["Id","MoSold"],axis = 1,inplace = True)

            train_df,test_df = train_test_split(raw_df,test_size=0.2,random_state=42)

            train_df.to_csv(self.data_ingestion_config.training_data_path,index = False, header = True)
            test_df.to_csv(self.data_ingestion_config.testing_data_path,index = False, header = True)

            logging.info("Data loaded")

            return train_df
        except Exception as e:
            raise CustomException(e,sys)

if __name__ == '__main__':
    data_ingestion = DataIngestion()
    train_df, test_df = data_ingestion.initiate_data_ingestion()
    # data_transformation = DataTransformation()
    # preprocessed_train_df,preprocessed_test_df, preprocessor_path = data_transformation.initiate_data_transformation(train_df, test_df)
    # model_trainer = ModelTrainer()
    # model_trainer.initiate_model_training(preprocessed_train_df,preprocessed_test_df)
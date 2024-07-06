import os,sys
from src.logger import logging
from src.exception import CustomException
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split


from dataclasses import dataclass

@dataclass
class DataIngestionConfig:
    raw_data_path = os.path.join('artifacts','raw_data.csv')
    train_data_path = os.path.join('artifacts','train.csv')
    test_data_path = os.path.join('artifacts','test.csv')


class DataIngestion:
    def __init__(self):
        self.ingestion_config = DataIngestionConfig()


    def initiate_data_ingestion(self):
        try:
            # Reading data from the folder in local pc
            df = pd.read_csv(r'D:\DS-AB\Project\MLOps_Project\dataset\raw dataset.csv')
            logging.info("reading data from local system")

            #Creating directory to store raw and splitted datasets
            os.makedirs(os.path.dirname(self.ingestion_config.raw_data_path), exist_ok=True) #creating artifacts folder
            df.to_csv(self.ingestion_config.raw_data_path,index=False, header=True) # saving raw dataset in csv folder in dataframe format

            #splitting raw date into train & test
            train_set, test_set = train_test_split(df, test_size=.2 ,random_state=42)
            logging.info("Dataset splitted successfully")
            
            #Saving splitted data 
            train_set.to_csv(self.ingestion_config.train_data_path,index=False, header=True)
            test_set.to_csv(self.ingestion_config.test_data_path,index=False, header=True)
            logging.info("splitted dataset saved successfully")

            #returing files path
            return(
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path )

        except Exception as e:
            raise CustomException(e,sys)
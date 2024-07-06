from src.logger import logging
import sys
from src.exception import CustomException
from src.components.data_ingestion import DataIngestionConfig, DataIngestion


if __name__ == '__main__':

    try:
        data_ingestion_obj = DataIngestion()
        data_ingestion_obj.initiate_data_ingestion()
    
    except Exception as e:
        logging.info("Custom exception")
        raise CustomException(e,sys)
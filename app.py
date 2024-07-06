from src.logger import logging
import sys
from src.exception import CustomException


if __name__ == '__main__':
    logging.info("successfully tested log generation ")

    try:
        a =10/0
    
    except Exception as e:
        logging.info("Custom exception")
        raise CustomException(e,sys)
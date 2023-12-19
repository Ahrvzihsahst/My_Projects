import os
import sys
from src.Exception import CustomException
from src.Logger import logging
import pandas as pd

from sklearn.model_selection import train_test_split
from dataclasses import dataclass

@dataclass
class DataIngetionConfig:
    train_data_path: str = os.path.join('Data_folder','train.csv')
    test_data_path: str = os.path.join('Data_folder','test.csv')
    raw_data_path: str = os.path.join('Data_folder','raw.csv')


class DataIngetion:
    def __init__(self):
        self.ingetion_config = DataIngetionConfig()

    def initiate_data_ingetion(self):
        # Read the data souce
         logging.info("Entered the data ingetion method")
         try:
             df = pd.read_csv("D:\My Prog\Github\My_Projects\Data Science\Machine Learning\Student_mark_prediction\src\stud.csv")
             logging.info("Read the dataset as dataframe")


             os.makedirs(os.dirname(self.ingetion_config.train_data_path),exist_ok = True)

             df.to_csv(self.ingetion_config.raw_data_path,index = False, header = True)

             logging.info("Train_test_splity initiated")   
             train_set,test_set = train_test_split(df,test_size=0.2, random_sate=0)

             train_set.to_csv(self.ingetion_config.train_data_path,index = False, header = True )
             test_set.to_csv(self.ingetion_config.test_data_path,index = False, header = True )
             
             logging.info("Ingetion of the data is completed")

             return(
                 self.ingetion_config.train_data_path,
                 self.ingetion_config.test_data_path,
             )
         except Exception as e: 
             raise CustomException(e,sys)

if __name__ =="__main__":
    obj = DataIngetion()
    obj.initiate_data_ingetion()

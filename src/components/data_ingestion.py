import shutil
import sys
import pandas as pd

from src.entity.config_entity import DataIngestionConfig
from src.exception import CustomException
from src.logger import logging

class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config
    def initiate_data_ingestion(self):
        try:
            logging.info("Starting data ingestion...")
            source=self.config.source_file
            destination=self.config.local_data_file

            df = pd.read_csv(
                    source,
                    sep="\t",
                    header=None,
                    names=["label", "message"]
                )
            self.config.root_dir.mkdir(
                parents=True,
                exist_ok=True
            )
            df.to_csv(
            self.config.local_data_file,
            index=False
            )
            
            logging.info(
                f"Dataset successfully saved to "
                f"{self.config.local_data_file}"
            )

        except Exception as e:
            logging.exception("Data ingestion failed.")
            raise CustomException(e, sys)

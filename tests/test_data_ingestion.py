from src.config.configuration import ConfigurationManager
from src.components.data_ingestion import DataIngestion

config=ConfigurationManager()

ingestion_config=config.get_data_ingestion_config()

data_ingestion=DataIngestion(ingestion_config)

data_ingestion.initiate_data_ingestion()
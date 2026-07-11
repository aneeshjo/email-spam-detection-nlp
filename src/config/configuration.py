from pathlib import Path


from src.constants import CONFIG_FILE_PATH, PARAMS_FILE_PATH
from src.entity.config_entity import (
    DataIngestionConfig,
    DataValidationConfig
)
from src.utils.common import read_yaml, create_directories

class ConfigurationManager:

    def __init__(self):
        self.config=read_yaml(CONFIG_FILE_PATH)
        self.params=read_yaml(PARAMS_FILE_PATH)

        create_directories([self.config.artifacts_root])

    def get_data_ingestion_config(
    self
    ) -> DataIngestionConfig:
        
        config = self.config.data_ingestion
        create_directories([config.root_dir])

        data_ingestion_config = DataIngestionConfig(
            root_dir=Path(config.root_dir),
            source_file=Path(config.source_file),
            local_data_file=Path(config.local_data_file)
        )

        return data_ingestion_config
    
    def get_data_validation_config(self) -> DataValidationConfig:
        """
        Creates and returns the configuration required for
        the Data Validation component.
        """

        config = self.config.data_validation

        create_directories([config.root_dir])

        data_validation_config = DataValidationConfig(
            root_dir=Path(config.root_dir),
            status_file=Path(config.status_file),
            data_file=Path(
                self.config.data_ingestion.local_data_file
            )
        )

        return data_validation_config
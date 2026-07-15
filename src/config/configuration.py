from pathlib import Path


from src.constants import CONFIG_FILE_PATH, PARAMS_FILE_PATH
from src.entity.config_entity import (
    DataIngestionConfig,
    DataValidationConfig,
    DataTransformationConfig,
    ModelTrainerConfig,
    ModelEvaluationConfig,
    HuggingFaceConfig
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
    
    def get_data_transformation_config(self) -> DataTransformationConfig:
        config=self.config.data_transformation
        create_directories([config.root_dir])

        data_transformation_config=DataTransformationConfig(
            root_dir=Path(config.root_dir),
            input_data_file=Path(config.input_data_file),
            transformed_data_file=Path(config.transformed_data_file)
           
        )
        return data_transformation_config
    def get_model_trainer_config(self) -> ModelTrainerConfig:

        config = self.config.model_trainer

        create_directories([config.root_dir])

        model_trainer_config = ModelTrainerConfig(
            root_dir=Path(config.root_dir),
            input_data_file=Path(config.input_data_file),
            model_file=Path(config.model_file),
            vectorizer_file=Path(config.vectorizer_file),

            test_size=self.params.TEST_SIZE,
            random_state=self.params.RANDOM_STATE,
            stratify=self.params.STRATIFY
        )

        return model_trainer_config
    
    def get_model_evaluation_config(
        self
    ) -> ModelEvaluationConfig:

        config = self.config.model_evaluation

        create_directories([config.root_dir])

        model_evaluation_config = ModelEvaluationConfig(
            root_dir=Path(config.root_dir),
            input_data_file=Path(config.input_data_file),
            model_file=Path(config.model_file),
            vectorizer_file=Path(config.vectorizer_file),
            metric_file=Path(config.metric_file),

            test_size=self.params.TEST_SIZE,
            random_state=self.params.RANDOM_STATE,
            stratify=self.params.STRATIFY
        )

        return model_evaluation_config
    
    def get_huggingface_config(self) -> HuggingFaceConfig:

        config = self.config.huggingface

        huggingface_config = HuggingFaceConfig(
        repo_id=config.repo_id,
        model_file=config.model_file,
        vectorizer_file=config.vectorizer_file
        )

        return huggingface_config
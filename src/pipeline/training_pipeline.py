import sys

from src.components.data_ingestion import DataIngestion
from src.components.data_validation import DataValidation
from src.components.data_transformation import DataTransformation
from src.components.model_trainer import ModelTrainer
from src.components.model_evaluation import ModelEvaluation

from src.config.configuration import ConfigurationManager

from src.exception import CustomException
from src.logger import logging

class TrainingPipeline:
    """
    Executes the complete NLP training pipeline.
    """

    def __init__(self):
        """
        Initialize the training pipeline.
        """

        self.config = ConfigurationManager()

        logging.info("Training Pipeline Initialized.")

    def run_pipeline(self):
        """
        Execute the complete training pipeline.
        """

        try:

            # =====================================================
            # Data Ingestion
            # =====================================================

            logging.info("========== Data Ingestion Started ==========")

            ingestion_config = self.config.get_data_ingestion_config()

            data_ingestion = DataIngestion(ingestion_config)

            data_ingestion.initiate_data_ingestion()

            logging.info("========== Data Ingestion Completed ==========")

            # =====================================================
            # Data Validation
            # =====================================================

            logging.info("========== Data Validation Started ==========")

            validation_config = self.config.get_data_validation_config()

            data_validation = DataValidation(validation_config)

            data_validation.validate_dataset()

            logging.info("========== Data Validation Completed ==========")

            # =====================================================
            # Data Transformation
            # =====================================================

            logging.info("========== Data Transformation Started ==========")

            transformation_config = self.config.get_data_transformation_config()

            data_transformation = DataTransformation(
                transformation_config
            )

            data_transformation.initiate_data_transformation()

            logging.info("========== Data Transformation Completed ==========")

            # =====================================================
            # Model Training
            # =====================================================

            logging.info("========== Model Training Started ==========")

            trainer_config = self.config.get_model_trainer_config()

            model_trainer = ModelTrainer(trainer_config)

            model_trainer.initiate_model_training()

            logging.info("========== Model Training Completed ==========")

            # =====================================================
            # Model Evaluation
            # =====================================================

            logging.info("========== Model Evaluation Started ==========")

            evaluation_config = self.config.get_model_evaluation_config()

            model_evaluation = ModelEvaluation(
                evaluation_config
            )
            model, vectorizer = model_evaluation.load_artifacts()

            df = model_evaluation.load_data()


            model_evaluation.evaluate_model(model=model,vectorizer=vectorizer,df=df)

            logging.info("========== Model Evaluation Completed ==========")

            logging.info(
                "========== Training Pipeline Finished Successfully =========="
            )

        except Exception as e:
            raise CustomException(e, sys)
import sys

from src.pipeline.training_pipeline import TrainingPipeline
from src.exception import CustomException
from src.logger import logging


def main():
    """
    Execute the complete training pipeline.
    """

    try:

        logging.info("=" * 60)
        logging.info("Email Spam Detection Training Started")
        logging.info("=" * 60)

        pipeline = TrainingPipeline()

        pipeline.run_pipeline()

        logging.info("=" * 60)
        logging.info("Training Completed Successfully")
        logging.info("=" * 60)

    except Exception as e:
        raise CustomException(e, sys)


if __name__ == "__main__":
    main()
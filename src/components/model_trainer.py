import sys

import joblib
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import LinearSVC

from src.entity.config_entity import ModelTrainerConfig
from src.exception import CustomException
from src.logger import logging

class ModelTrainer:
    """
    Handles model training for the Email Spam Detection project.

    Responsibilities:
    1. Load the cleaned dataset.
    2. Split the data into training and testing sets.
    3. Train the TF-IDF vectorizer.
    4. Train the Linear SVM model.
    5. Save the trained model and vectorizer.
    """

    def __init__(self, config: ModelTrainerConfig):
        """
        Initialize the ModelTrainer component.

        Parameters
        ----------
        config : ModelTrainerConfig
            Configuration object containing all required paths.
        """

        self.config = config

        logging.info("ModelTrainer component initialized successfully.")

    def load_data(self) -> pd.DataFrame:
        """
        Load the cleaned dataset for model training.

        Returns
        -------
        pd.DataFrame
            The cleaned dataset.
        """

        try:

            logging.info("Loading cleaned dataset...")

            df = pd.read_csv(
                self.config.input_data_file,
                keep_default_na=False
            )

            required_columns = [
                "label",
                "message",
                "transformed_text"
            ]

            missing_columns = [
                column
                for column in required_columns
                if column not in df.columns
            ]

            if missing_columns:
                raise ValueError(
                    f"Missing required columns: {missing_columns}"
                )

            logging.info(
                f"Dataset loaded successfully with shape: {df.shape}"
            )

            return df

        except Exception as e:
            logging.exception("Failed to load the data")
            raise CustomException(e, sys)
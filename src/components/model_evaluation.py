import json
import sys

import joblib
import pandas as pd

from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    confusion_matrix
)

from src.utils.models_utils import split_dataset
from src.entity.config_entity import ModelEvaluationConfig
from src.exception import CustomException
from src.logger import logging

class ModelEvaluation:
    """
    Handles evaluation of the trained spam classification model.

    Responsibilities
    ----------------
    1. Load trained model and vectorizer.
    2. Load cleaned dataset.
    3. Recreate train-test split.
    4. Generate predictions.
    5. Calculate evaluation metrics.
    6. Save metrics to JSON.
    """

    def __init__(self, config: ModelEvaluationConfig):
        """
        Initialize the ModelEvaluation component.

        Parameters
        ----------
        config : ModelEvaluationConfig
            Configuration object containing required paths.
        """

        self.config = config

        logging.info(
            "ModelEvaluation component initialized successfully."
        )

    def load_artifacts(self):
        """
        Load the trained model and fitted TF-IDF vectorizer.

        Returns
        -------
        tuple
            (model, vectorizer)
        """

        try:

            logging.info("Loading trained model and TF-IDF vectorizer...")

            # Load trained Linear SVM model
            model = joblib.load(
                self.config.model_file
            )

            logging.info(
                f"Model loaded from: {self.config.model_file}"
            )

            # Load fitted TF-IDF vectorizer
            vectorizer = joblib.load(
                self.config.vectorizer_file
            )

            logging.info(
                f"Vectorizer loaded from: {self.config.vectorizer_file}"
            )

            return model, vectorizer

        except Exception as e:
            raise CustomException(e, sys)
        
    def load_data(self) -> pd.DataFrame:
        """
        Load the cleaned dataset for model evaluation.

        Returns
        -------
        pd.DataFrame
            Cleaned dataset.
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
            raise CustomException(e, sys)
        

    def evaluate_model(
    self,
    model,
    vectorizer,
    df: pd.DataFrame
    ):
        """
        Evaluate the trained model on the test dataset.

        Parameters
        ----------
        model : LinearSVC
            Trained spam classification model.

        vectorizer : TfidfVectorizer
            Fitted TF-IDF vectorizer.

        df : pd.DataFrame
            Cleaned dataset.

        Returns
        -------
        dict
            Dictionary containing evaluation metrics.
        """

        try:

            logging.info("Starting model evaluation...")

            

            X_train, X_test, y_train, y_test = split_dataset(
                    df,
                    self.config
                )
            # =====================================================
            # Transform Test Data
            # =====================================================

            X_test_vectorized = vectorizer.transform(X_test)

            logging.info("Test data transformed successfully.")

            # =====================================================
            # Predictions
            # =====================================================

            y_pred = model.predict(X_test_vectorized)

            logging.info("Predictions generated successfully.")

            # =====================================================
            # Calculate Metrics
            # =====================================================
            logging.info(f"Unique values in y_test: {y_test.unique()}")
            logging.info(f"Unique values in y_pred: {pd.Series(y_pred).unique()}")

            
            metrics = {
                "accuracy": accuracy_score(y_test, y_pred),
                "precision": precision_score(y_test, y_pred),
                "recall": recall_score(y_test, y_pred),
                "f1_score": f1_score(y_test, y_pred),
                "confusion_matrix": confusion_matrix(
                    y_test,
                    y_pred
                ).tolist()
            }

            logging.info("Evaluation metrics calculated successfully.")

            return metrics

        except Exception as e:
            raise CustomException(e, sys)
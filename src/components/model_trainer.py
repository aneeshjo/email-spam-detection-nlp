import sys

import joblib
import pandas as pd

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import LinearSVC

from src.entity.config_entity import ModelTrainerConfig
from src.exception import CustomException
from src.logger import logging
from src.utils.models_utils import split_dataset

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
        
    
        
    def train_vectorizer(
    self,
    X_train,
    X_test
    ):
        """
        Train the TF-IDF vectorizer using only the training data.

        Parameters
        ----------
        X_train : pd.Series
            Training text data.

        X_test : pd.Series
            Testing text data.

        Returns
        -------
        tuple
            X_train_vectorized,
            X_test_vectorized,
            fitted_vectorizer
        """

        try:

            logging.info("Training TF-IDF vectorizer...")

            # Initialize TF-IDF
            vectorizer = TfidfVectorizer()

            # Learn vocabulary from training data
            X_train_vectorized = vectorizer.fit_transform(X_train)

            # Transform testing data using the same vocabulary
            X_test_vectorized = vectorizer.transform(X_test)

            logging.info(
                f"Vocabulary Size : {len(vectorizer.vocabulary_)}"
            )

            logging.info(
                "TF-IDF vectorization completed successfully."
            )

            return (
                X_train_vectorized,
                X_test_vectorized,
                vectorizer
            )

        except Exception as e:
            raise CustomException(e, sys)
        
    def train_model(
    self,
    X_train_vectorized,
    y_train
    ):
        """
        Train the Linear Support Vector Machine classifier.

        Parameters
        ----------
        X_train_vectorized : sparse matrix
            TF-IDF transformed training data.

        y_train : pd.Series
            Training labels.

        Returns
        -------
        LinearSVC
            Trained Linear SVM model.
        """

        try:

            logging.info("Training Linear SVM model...")

            # Initialize the model
            model = LinearSVC(
                random_state=42,
                dual="auto"
            )

            # Train the model
            model.fit(
                X_train_vectorized,
                y_train
            )

            logging.info("Model training completed successfully.")

            return model

        except Exception as e:
            raise CustomException(e, sys)
        
    def save_artifacts(
    self,
    model,
    vectorizer
    ):
        """
        Save the trained model and fitted TF-IDF vectorizer.

        Parameters
        ----------
        model : LinearSVC
            Trained Linear SVM model.

        vectorizer : TfidfVectorizer
            Fitted TF-IDF vectorizer.
        """

        try:

            logging.info("Saving trained artifacts...")

            # Save trained model
            joblib.dump(
                model,
                self.config.model_file
            )

            logging.info(
                f"Model saved at: {self.config.model_file}"
            )

            # Save fitted vectorizer
            joblib.dump(
                vectorizer,
                self.config.vectorizer_file
            )

            logging.info(
                f"Vectorizer saved at: {self.config.vectorizer_file}"
            )

            logging.info(
                "Artifacts saved successfully."
            )

        except Exception as e:
            raise CustomException(e, sys)
        
    def initiate_model_training(self):
        """
        Execute the complete model training pipeline.
        """

        try:

            logging.info("Starting model training pipeline...")

            # ==========================================
            # Load cleaned dataset
            # ==========================================

            df = self.load_data()

            # ==========================================
            # Split dataset
            # ==========================================

            X_train, X_test, y_train, y_test = split_dataset(
                df,
                self.config
            )

            # ==========================================
            # Train TF-IDF Vectorizer
            # ==========================================

            (
                X_train_vectorized,
                X_test_vectorized,
                vectorizer
            ) = self.train_vectorizer(
                X_train,
                X_test
            )

            # ==========================================
            # Train Linear SVM
            # ==========================================

            model = self.train_model(
                X_train_vectorized,
                y_train
            )

            # ==========================================
            # Save Artifacts
            # ==========================================

            self.save_artifacts(
                model,
                vectorizer
            )

            logging.info(
                "Model training pipeline completed successfully."
            )

        except Exception as e:
            raise CustomException(e, sys)
import sys

import joblib

from src.exception import CustomException
from src.logger import logging
from src.utils.text_utils import transform_text
from src.config.configuration import PredictionConfig

class CustomData:
    """
    Represents a single SMS message provided by the user.
    """

    def __init__(
        self,
        message: str
    ):

        self.message = message

    def get_processed_text(self):
        """
        Apply text preprocessing to the user input.

        Returns
        -------
        str
            Cleaned text.
        """

        return transform_text(
            self.message
        )
    
class PredictionPipeline:
    """
    Handles loading the trained artifacts and making predictions
    on new SMS messages.
    """

    def __init__(
        self,
        config:PredictionConfig
    ):
        """
        Initialize the PredictionPipeline.

        Parameters
        ----------
        model_path : str
            Path to the trained model.

        vectorizer_path : str
            Path to the fitted TF-IDF vectorizer.
        """
        self.config=config

        try:

            logging.info("Loading prediction artifacts...")

            self.model = joblib.load(config.model_file)

            self.vectorizer = joblib.load(config.vectorizer_file)

            logging.info(
                "Prediction artifacts loaded successfully."
            )

        except Exception as e:
            raise CustomException(e, sys)
        
    def predict(self, processed_text: str):
        """
        Predict whether an SMS message is Ham or Spam.

        Parameters
        ----------
        processed_text : str
            Preprocessed SMS message.

        Returns
        -------
        int
            Predicted class.
            0 -> Ham
            1 -> Spam
        """

        try:

            logging.info("Vectorizing input text...")

            # Convert text into TF-IDF features
            transformed_text = self.vectorizer.transform(
                [processed_text]
            )

            logging.info("Generating prediction...")

            prediction = self.model.predict(
                transformed_text
            )[0]

            logging.info(
                f"Prediction completed successfully: {prediction}"
            )

            return prediction

        except Exception as e:
            raise CustomException(e, sys)
        
    def predict_label(self, processed_text: str) -> dict:
        """
        Predict the class label for an SMS message.

        Parameters
        ----------
        processed_text : str
            Preprocessed SMS message.

        Returns
        -------
        dict
            Dictionary containing prediction and label.
        """

        try:

            prediction = self.predict(processed_text)

            result = {
                0: "Ham",
                1: "Spam"
            }

            return {
                "prediction": prediction,
                "label": result[prediction]
            }

        except Exception as e:
            raise CustomException(e, sys)
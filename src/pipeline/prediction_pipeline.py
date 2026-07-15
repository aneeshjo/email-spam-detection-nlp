import sys

import joblib

from src.exception import CustomException
from src.logger import logging
from src.utils.text_utils import transform_text
from src.entity.config_entity import HuggingFaceConfig
from src.utils.huggingface_utils import HuggingFaceDownloader


class CustomData:
    """
    Represents a single SMS message provided by the user.
    """

    def __init__(
        self,
        message: str
    ):
        self.message = message

    def get_processed_text(self) -> str:
        """
        Apply text preprocessing to the user input.

        Returns
        -------
        str
            Cleaned text.
        """

        return transform_text(self.message)


class PredictionPipeline:
    """
    Loads the trained model and vectorizer from
    Hugging Face and performs predictions.
    """

    def __init__(
        self,
        config: HuggingFaceConfig
    ):

        self.config = config

        try:

            logging.info(
                "Initializing Prediction Pipeline..."
            )

            # -----------------------------------------
            # Download Artifacts
            # -----------------------------------------

            downloader = HuggingFaceDownloader(
                repo_id=config.repo_id
            )

            model_path = downloader.download_file(
                config.model_file
            )

            vectorizer_path = downloader.download_file(
                config.vectorizer_file
            )

            # -----------------------------------------
            # Load Artifacts
            # -----------------------------------------

            logging.info(
                "Loading trained model..."
            )

            self.model = joblib.load(
                model_path
            )

            logging.info(
                "Loading TF-IDF vectorizer..."
            )

            self.vectorizer = joblib.load(
                vectorizer_path
            )

            logging.info(
                "Prediction Pipeline initialized successfully."
            )

        except Exception as e:
            raise CustomException(e, sys)

    def predict(
        self,
        processed_text: str
    ) -> int:
        """
        Predict whether an SMS is Ham or Spam.

        Parameters
        ----------
        processed_text : str

        Returns
        -------
        int

            0 -> Ham

            1 -> Spam
        """

        try:

            logging.info(
                "Vectorizing input text..."
            )

            transformed_text = self.vectorizer.transform(
                [processed_text]
            )

            logging.info(
                "Generating prediction..."
            )

            prediction = self.model.predict(
                transformed_text
            )[0]

            logging.info(
                f"Prediction completed successfully: {prediction}"
            )

            return prediction

        except Exception as e:
            raise CustomException(e, sys)

    def predict_label(
        self,
        processed_text: str
    ) -> dict:
        """
        Return prediction and corresponding label.
        """

        try:

            prediction = self.predict(
                processed_text
            )

            label_mapping = {
                0: "Ham",
                1: "Spam"
            }

            return {
                "prediction": prediction,
                "label": label_mapping[prediction]
            }

        except Exception as e:
            raise CustomException(e, sys)
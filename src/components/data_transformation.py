import string
import sys
import joblib
import pandas as pd
import nltk

from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize

from src.utils.text_utils import transform_text
from src.entity.config_entity import DataTransformationConfig
from src.exception import CustomException
from src.logger import logging

class DataTransformation:
    """
    Handles text preprocessing and TF-IDF vectorization
    for the Email Spam Detection project.
    """

    def __init__(self, config: DataTransformationConfig):
        """
        Initialize the DataTransformation component.

        Parameters
        ----------
        config : DataTransformationConfig
            Configuration object containing all required paths.
        """

        self.config = config
       
        logging.info("DataTransformation component initialized successfully.")

    
    
    def initiate_data_transformation(self):
        """
        Executes the complete data transformation pipeline.

        Steps:
        1. Load the dataset.
        2. Apply text preprocessing.
        3. Create the transformed_text column.
        4. Train the TF-IDF vectorizer.
        5. Save the transformed dataset.
        6. Save the fitted TF-IDF vectorizer.
        """

        try:

            logging.info("Starting data transformation...")
            # ======================================================
            # Load Dataset
            # ======================================================

            df=pd.read_csv(self.config.input_data_file,keep_default_na=False)

            logging.info(
            f"Dataset loaded successfully with shape: {df.shape}"
            )
            # ======================================================
            # Encode Labels
            # ======================================================

            label_mapping = {
                "ham": 0,
                "spam": 1
            }

            df["label"] = df["label"].map(label_mapping)

            logging.info("Labels encoded successfully.")

            # ======================================================
            # Text Preprocessing
            # ======================================================

            df["transformed_text"] = df["message"].apply(
            transform_text
            )

            logging.info( "Text preprocessing completed successfully.")
            
            # ======================================================
            # Save Transformed Dataset
            # ======================================================
            df.to_csv(
                self.config.transformed_data_file,
                index=False
            )

            logging.info(
            f"Transformed dataset saved at: {self.config.transformed_data_file}"
            )

            # ======================================================
            # Save Vectorizer
            # ======================================================

            logging.info(
            "Data transformation completed successfully."
            )

        except Exception as e:
            
            raise CustomException(e, sys)





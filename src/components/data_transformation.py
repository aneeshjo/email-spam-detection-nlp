import string
import sys
import joblib
import pandas as pd
import nltk

from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize

from sklearn.feature_extraction.text import TfidfVectorizer

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

        # Initialize the English stopword set
        self.stop_words = set(stopwords.words("english"))

        # Initialize the Porter Stemmer
        self.stemmer = PorterStemmer()

        logging.info("DataTransformation component initialized successfully.")

    def _transform_text(self, message: str) -> str:
        """
        Preprocess a single SMS message.

        Steps:
        1. Convert text to lowercase.
        2. Tokenize the text.
        3. Remove non-alphanumeric tokens.
        4. Remove English stopwords.
        5. Apply Porter Stemming.
        6. Join tokens back into a string.

        Parameters
        ----------
        message : str
            Input SMS message.

        Returns
        -------
        str
            Cleaned and preprocessed message.
        """

        # Convert to lower case -1
        message=str(message).lower()

        # Tokenize the word -2
        tokens=word_tokenize(message)

        # Remove Special Characters-3
        tokens=[token for token in tokens if token.isalnum()]

        # Remove Stop words -4
        tokens=[token for token in tokens if token not in self.stop_words]

        # Applying Stemmig
        # Apply stemming
        tokens = [
        self.stemmer.stem(token)
        for token in tokens
        ]

        # Return cleaned text
        return " ".join(tokens)


import nltk
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize


# Download required NLTK resources if missing
try:
    nltk.data.find("corpora/stopwords")
except LookupError:
    nltk.download("stopwords")

try:
    nltk.data.find("tokenizers/punkt")
except LookupError:
    nltk.download("punkt")

# Needed for newer NLTK versions
try:
    nltk.data.find("tokenizers/punkt_tab")
except LookupError:
    nltk.download("punkt_tab")

# Initialize once
stop_words = set(stopwords.words("english"))
stemmer = PorterStemmer()

def transform_text(message: str) -> str:
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
    tokens=[token for token in tokens if token not in stop_words]

    # Applying Stemmig
        
    tokens = [
    stemmer.stem(token)
    for token in tokens
    ]

    # Return cleaned text
    return " ".join(tokens)
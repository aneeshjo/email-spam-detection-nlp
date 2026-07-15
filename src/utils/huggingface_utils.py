import os

from huggingface_hub import hf_hub_download

from src.logger import logging


class HuggingFaceDownloader:
    """
    Downloads model artifacts from Hugging Face Hub.
    """

    def __init__(
        self,
        repo_id: str,
        cache_dir: str = "artifacts/model_trainer"
    ):

        self.repo_id = repo_id
        self.cache_dir = cache_dir

    def download_file(
        self,
        filename: str
    ) -> str:
        """
        Download a file from Hugging Face and return its local path.
        """

        logging.info(
            f"Downloading {filename} from Hugging Face..."
        )

        path = hf_hub_download(
            repo_id=self.repo_id,
            filename=filename,
            cache_dir=self.cache_dir
        )

        logging.info(
            f"{filename} downloaded successfully."
        )

        return path
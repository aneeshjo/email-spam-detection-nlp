from src.config.configuration import ConfigurationManager
from src.components.data_validation import DataValidation

config = ConfigurationManager()

validation_config = config.get_data_validation_config()

validator = DataValidation(validation_config)

print(validator.validate_dataset())
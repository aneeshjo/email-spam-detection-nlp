from src.config.configuration import ConfigurationManager
from src.components.data_transformation import DataTransformation

# Load configuration
config = ConfigurationManager()

# Get Data Transformation configuration
transformation_config = config.get_data_transformation_config()

# Create DataTransformation object
transformation = DataTransformation(transformation_config)

# Execute data transformation
transformation.initiate_data_transformation()

print("Data Transformation completed successfully.")
from src.config.configuration import ConfigurationManager
from src.components.model_trainer import ModelTrainer

config = ConfigurationManager()

trainer_config = config.get_model_trainer_config()

trainer = ModelTrainer(trainer_config)

trainer.initiate_model_training()

print("Model training completed successfully.")
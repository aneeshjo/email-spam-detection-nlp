from src.pipeline.prediction_pipeline import (
    PredictionPipeline,
    CustomData
)
from src.config.configuration import ConfigurationManager

config = ConfigurationManager()

hf_config = config.get_huggingface_config()

pipeline = PredictionPipeline(hf_config)

# Test Message
custom_data = CustomData(
     message="Hi, are we still meeting at 6 PM today?"
)

processed_text = custom_data.get_processed_text()

prediction = pipeline.predict_label(processed_text)

print("Processed Text :", processed_text)
print("Prediction :", prediction)
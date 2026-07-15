from src.config.configuration import ConfigurationManager
from src.components.model_evaluation import ModelEvaluation

config = ConfigurationManager()

evaluation_config = config.get_model_evaluation_config()

evaluation = ModelEvaluation(evaluation_config)

model, vectorizer = evaluation.load_artifacts()

df = evaluation.load_data()

metrics = evaluation.evaluate_model(
    model,
    vectorizer,
    df
)

print(metrics)
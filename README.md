# 📧 Email Spam Detection using Natural Language Processing

![Python](https://img.shields.io/badge/Python-3.12-blue?style=for-the-badge&logo=python)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-ML-orange?style=for-the-badge&logo=scikitlearn)
![NLP](https://img.shields.io/badge/NLP-TF--IDF-green?style=for-the-badge)
![Streamlit](https://img.shields.io/badge/Streamlit-App-red?style=for-the-badge&logo=streamlit)
![License](https://img.shields.io/badge/License-MIT-blue?style=for-the-badge)

---

## 📌 Project Overview

This project is a **production-ready End-to-End Email/SMS Spam Detection System** developed using **Natural Language Processing (NLP)** and **Machine Learning**.

Unlike a traditional Jupyter Notebook project, this application follows a modular software engineering architecture with separate components for data ingestion, validation, transformation, model training, evaluation, and prediction.

The application classifies an incoming Email/SMS message as either:

- ✅ Ham (Legitimate Message)
- 🚨 Spam (Unwanted Message)

using a **TF-IDF Vectorizer** and a **Linear Support Vector Machine (LinearSVC)** classifier.

---

# 🎯 Objectives

- Learn traditional NLP from scratch.
- Understand text preprocessing techniques.
- Compare multiple Machine Learning algorithms.
- Build a production-ready modular architecture.
- Deploy the model using Streamlit.
- Follow software engineering best practices for AI/ML projects.

---

# 🚀 Features

- End-to-End NLP Pipeline
- Modular Project Structure
- Data Validation
- Data Transformation
- TF-IDF Feature Extraction
- Linear SVM Classifier
- Model Evaluation
- Prediction Pipeline
- Training Pipeline
- Streamlit Web Application
- Logging & Exception Handling
- Configuration Management using YAML

---

# 📂 Project Structure

```text
Email-Spam-Detection
│
├── app.py
├── main.py
├── requirements.txt
├── setup.py
│
├── config
│   ├── config.yaml
│   └── params.yaml
│
├── artifacts
│   ├── data_ingestion
│   ├── data_validation
│   ├── data_transformation
│   ├── model_trainer
│   └── model_evaluation
│
├── logs
│
├── src
│   ├── components
│   │   ├── data_ingestion.py
│   │   ├── data_validation.py
│   │   ├── data_transformation.py
│   │   ├── model_trainer.py
│   │   └── model_evaluation.py
│   │
│   ├── config
│   │   └── configuration.py
│   │
│   ├── entity
│   │   └── config_entity.py
│   │
│   ├── pipeline
│   │   ├── prediction.py
│   │   └── training_pipeline.py
│   │
│   ├── utils
│   │   ├── common.py
│   │   ├── text_utils.py
│   │   └── model_utils.py
│   │
│   ├── logger.py
│   └── exception.py
│
└── tests
```

---

# 📊 Dataset

**SMS Spam Collection Dataset**

- Total Messages: **5,572**
- Ham Messages: **4,825**
- Spam Messages: **747**

Each message is labelled as:

- Ham
- Spam

---

# 🔄 NLP Workflow

```text
Raw Text
      │
      ▼
Lowercase
      │
      ▼
Tokenization
      │
      ▼
Remove Special Characters
      │
      ▼
Remove Stopwords
      │
      ▼
Porter Stemming
      │
      ▼
Clean Text
      │
      ▼
TF-IDF Vectorization
      │
      ▼
Linear SVM
      │
      ▼
Prediction
```

---

# ⚙️ Production Pipeline

```text
Data Ingestion
        │
        ▼
Data Validation
        │
        ▼
Data Transformation
        │
        ▼
Model Training
        │
        ▼
Model Evaluation
        │
        ▼
Prediction Pipeline
        │
        ▼
Streamlit Application
```

---

# 🧠 Machine Learning Model

Multiple Machine Learning models were evaluated during experimentation.

The final production model selected was:

| Component  | Model                                     |
| ---------- | ----------------------------------------- |
| Vectorizer | TF-IDF                                    |
| Classifier | Linear Support Vector Machine (LinearSVC) |

The model was selected based on its strong performance and generalization capability.

---

# 📈 Model Performance

| Metric    |      Score |
| --------- | ---------: |
| Accuracy  | **98.39%** |
| Precision | **98.52%** |
| Recall    | **89.26%** |
| F1 Score  | **93.66%** |

---

# 🛠 Technologies Used

- Python
- Pandas
- NumPy
- NLTK
- Scikit-Learn
- Joblib
- Streamlit
- YAML
- Git
- GitHub

---

# ▶️ Installation

Clone the repository

```bash
git clone https://github.com/aneeshjo/email-spam-detection-nlp.git
```

Navigate into the project

```bash
cd email-spam-detection-nlp
```

Create a virtual environment

```bash
python -m venv venv
```

Activate the environment

Windows

```bash
venv\Scripts\activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

# 🚀 Run Training Pipeline

```bash
python main.py
```

---

# 🌐 Run Streamlit Application

```bash
streamlit run app.py
```

---

# 🧪 Testing

Run individual component tests

```bash
python -m tests.test_data_ingestion
python -m tests.test_data_validation
python -m tests.test_data_transformation
python -m tests.test_model_trainer
python -m tests.test_model_evaluation
python -m tests.test_prediction_pipeline
python -m tests.test_training_pipeline
```

---

# 📸 Application

The Streamlit application allows users to:

- Enter an Email/SMS
- Preprocess the text
- Predict Spam/Ham
- View the processed text

---

# 🔮 Future Improvements

- Deep Learning based spam detection
- LSTM & GRU models
- Transformer models (BERT)
- Explainable AI
- REST API using FastAPI
- Docker Deployment
- CI/CD Pipeline
- Cloud Deployment

---

# 👨‍💻 Author

**Aneesh Jose**

Aspiring AI/ML Engineer passionate about Machine Learning, Deep Learning, Computer Vision and Natural Language Processing.

GitHub:
https://github.com/aneeshjo

LinkedIn:
(Add your LinkedIn URL)

---

# ⭐ Acknowledgements

- SMS Spam Collection Dataset
- Scikit-Learn Documentation
- NLTK Documentation
- Streamlit Documentation

---

## ⭐ If you found this project useful, consider giving it a star!

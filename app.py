import streamlit as st

from src.pipeline.prediction_pipeline import (
    PredictionPipeline,
    CustomData
)

from src.config.configuration import ConfigurationManager



# ==========================================================
# Page Configuration
# ==========================================================

st.set_page_config(
    page_title="Email Spam Detector",
    page_icon="📧",
    layout="centered"
)


# ==========================================================
# Load Prediction Pipeline (Cached)
# ==========================================================

@st.cache_resource
def load_prediction_pipeline():
    """
    Load the trained prediction pipeline only once.
    """

    config = ConfigurationManager()

    prediction_config = config.get_prediction_config()

    pipeline = PredictionPipeline(prediction_config)

    return pipeline


pipeline = load_prediction_pipeline()


# ==========================================================
# Header
# ==========================================================

st.title("📧 Email Spam Detection")

st.markdown(
    """
Detect whether an Email or SMS message is **Spam** or **Ham**
using a Machine Learning model built with **TF-IDF + Linear SVM**.
"""
)

st.divider()


# ==========================================================
# User Input
# ==========================================================

message = st.text_area(
    "Enter your message",
    height=200,
    placeholder="Type your email or SMS message here..."
)


# ==========================================================
# Prediction
# ==========================================================

if st.button("Predict", use_container_width=True):

    if message.strip() == "":

        st.warning("Please enter a message.")

    else:

        custom_data = CustomData(
            message=message
        )

        processed_text = custom_data.get_processed_text()

        result = pipeline.predict_label(
            processed_text
        )

        st.divider()

        st.subheader("Prediction")

        if result["prediction"] == 1:

            st.error("🚨 Spam Message")

        else:

            st.success("✅ Ham Message")

        with st.expander("Processed Text"):

            st.write(processed_text)
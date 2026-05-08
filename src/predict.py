
import os
import joblib
from preprocess import clean_text

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

MODEL_PATH = os.path.join(
    BASE_DIR,
    "model",
    "sentinelai_model.pkl"
)

VECTORIZER_PATH = os.path.join(
    BASE_DIR,
    "model",
    "tfidf_vectorizer.pkl"
)

model = joblib.load(MODEL_PATH)

vectorizer = joblib.load(VECTORIZER_PATH)

def moderation_decision(confidence, prediction):

    if prediction == 0 and confidence >= 0.90:
        return "HIGH_RISK"

    elif prediction == 0 and confidence >= 0.70:
        return "MEDIUM_RISK"

    elif prediction == 0:
        return "LOW_RISK"

    else:
        return "SAFE"

def predict_content(text):

    cleaned = clean_text(text)

    vectorized = vectorizer.transform([cleaned])

    prediction = model.predict(vectorized)[0]

    probabilities = model.predict_proba(vectorized)[0]

    confidence = max(probabilities)

    label = "SAFE" if prediction == 1 else "UNSAFE"

    risk_level = moderation_decision(
        confidence,
        prediction
    )

    result = {
        "prediction": int(prediction),
        "label": label,
        "confidence": round(float(confidence), 4),
        "risk_level": risk_level
    }

    return result

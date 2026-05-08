
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

# Explicit unsafe keywords

SEXUAL_KEYWORDS = {
    "blowjob",
    "nude",
    "porn",
    "sex",
    "fuck",
    "dick",
    "pussy",
    "bitch",
    "asshole",
    "slut",
    "boobs",
    "naked"
}

SPAM_KEYWORDS = {
    "free money",
    "click here",
    "win cash",
    "crypto giveaway",
    "claim reward",
    "lottery",
    "urgent response",
    "limited offer",
    "buy now",
    "earn money fast"
}

VIOLENCE_KEYWORDS = {
    "kill you",
    "murder",
    "shoot you",
    "bomb",
    "terrorist",
    "destroy your life",
    "stab you"
}

def rule_based_detection(text):

    lower_text = text.lower()

    # Sexual detection
    for keyword in SEXUAL_KEYWORDS:

        if keyword in lower_text:

            return {
                "prediction": 0,
                "label": "UNSAFE",
                "confidence": 0.99,
                "risk_level": "HIGH_RISK",
                "source": "RULE_BASED_SEXUAL"
            }

    # Spam detection
    for keyword in SPAM_KEYWORDS:

        if keyword in lower_text:

            return {
                "prediction": 0,
                "label": "UNSAFE",
                "confidence": 0.98,
                "risk_level": "HIGH_RISK",
                "source": "RULE_BASED_SPAM"
            }

    # Violence detection
    for keyword in VIOLENCE_KEYWORDS:

        if keyword in lower_text:

            return {
                "prediction": 0,
                "label": "UNSAFE",
                "confidence": 0.99,
                "risk_level": "HIGH_RISK",
                "source": "RULE_BASED_VIOLENCE"
            }

    return None

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

    # Rule-based moderation first
    rule_result = rule_based_detection(text)

    if rule_result is not None:
        return rule_result

    # ML moderation
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
        "risk_level": risk_level,
        "source": "ML_MODEL"
    }

    return result

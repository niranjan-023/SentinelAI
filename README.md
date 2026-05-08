# SentinelAI
## AI-Powered Content Moderation System

SentinelAI is a AI moderation API designed to detect unsafe, toxic, spam, sexual, violent, hateful, and offensive English text content using a hybrid moderation architecture.

It combines:
- Machine Learning (TF-IDF + Logistic Regression)
- Rule-Based Moderation
- FastAPI Backend
- Cloud Deployment on Render

---

# Live API

Base URL:

https://sentinelai-api-yc5z.onrender.com

Swagger Documentation:

https://sentinelai-api-yc5z.onrender.com/docs

---

# Features

- Toxic content detection
- Hate speech detection
- Offensive language detection
- Spam detection
- Sexual content detection
- Violence/threat detection
- Binary moderation output
- Confidence scoring
- Risk level classification
- Public REST API
- Swagger documentation
- Cloud deployment

---

# Moderation Labels

| Label | Meaning |
|---|---|
| 1 | SAFE |
| 0 | UNSAFE |

---

# Tech Stack

| Component | Technology |
|---|---|
| Language | Python |
| Machine Learning | Scikit-learn |
| NLP | TF-IDF |
| Model | Logistic Regression |
| Backend | FastAPI |
| Hosting | Render |
| Dataset Sources | Jigsaw + Spam + Hate Speech |

---

# Dataset Sources

The model was trained using a merged dataset created from:

- Jigsaw Toxic Comment Classification Dataset
- SMS Spam Collection Dataset
- Hate Speech and Offensive Language Dataset

Combined dataset size:
- ~189,000+ samples

---

# Project Architecture

```text
SentinelAI/
│
├── api/
│   └── main.py
│
├── src/
│   ├── preprocess.py
│   └── predict.py
│
├── model/
│   ├── sentinelai_model.pkl
│   └── tfidf_vectorizer.pkl
│
├── requirements.txt
├── runtime.txt
└── README.md
```

---

# Machine Learning Pipeline

```text
Input Text
    ↓
Rule-Based Moderation
    ↓
Text Preprocessing
    ↓
TF-IDF Vectorization
    ↓
Logistic Regression Prediction
    ↓
Confidence + Risk Classification
```

---

# Model Performance

| Metric | Score |
|---|---|
| Accuracy | 95% |
| F1 Score | 96.87% |

---

# API Endpoints

## Home Endpoint

### GET /

Response:

```json
{
  "message": "SentinelAI API is running"
}
```

---

## Health Check

### GET /health

Response:

```json
{
  "status": "healthy"
}
```

---

## Prediction Endpoint

### POST /predict

Request:

```json
{
  "text": "I will kill you"
}
```

Response:

```json
{
  "prediction": 0,
  "label": "UNSAFE",
  "confidence": 0.99,
  "risk_level": "HIGH_RISK",
  "source": "RULE_BASED_VIOLENCE"
}
```

---

# Risk Levels

| Risk Level | Meaning |
|---|---|
| SAFE | Safe content |
| LOW_RISK | Slightly unsafe |
| MEDIUM_RISK | Moderately unsafe |
| HIGH_RISK | Highly unsafe |

---

# Local Setup

## Clone Repository

```bash
git clone https://github.com/niranjan-023/SentinelAI.git
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Run API Locally

```bash
uvicorn api.main:app --reload
```

---

# Open Swagger Docs

```text
http://127.0.0.1:8000/docs
```

---

# Deployment

SentinelAI is deployed using:

- Render.com
- FastAPI
- Uvicorn

---

# Example Python API Usage

```python
import requests

url = "https://sentinelai-api-yc5z.onrender.com/predict"

payload = {
    "text": "You are amazing"
}

response = requests.post(url, json=payload)

print(response.json())
```

---

# Example Response

```json
{
  "prediction": 1,
  "label": "SAFE",
  "confidence": 0.91,
  "risk_level": "SAFE",
  "source": "ML_MODEL"
}
```

---
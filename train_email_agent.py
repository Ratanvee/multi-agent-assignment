import os
import joblib
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

# Create models/ directory if it doesn't exist
os.makedirs("models", exist_ok=True)


# Training data
emails = [
    "Please fix my issue immediately. This product is defective.",
    "Hello, I want to know more about your pricing plans.",
    "The service was great. Thank you!",
    "I need help with my order. It’s urgent.",
    "Can you explain the warranty policy?",
]

intent_labels = ["complaint", "query", "feedback", "complaint", "query"]
urgency_labels = ["high", "low", "low", "high", "low"]

# Pipeline for intent
intent_pipeline = Pipeline([
    ("tfidf", TfidfVectorizer()),
    ("clf", LogisticRegression())
])
intent_pipeline.fit(emails, intent_labels)
joblib.dump(intent_pipeline, "models/email_intent_model.pkl")

# Pipeline for urgency
urgency_pipeline = Pipeline([
    ("tfidf", TfidfVectorizer()),
    ("clf", LogisticRegression())
])
urgency_pipeline.fit(emails, urgency_labels)
joblib.dump(urgency_pipeline, "models/email_urgency_model.pkl")

print("Email intent and urgency models saved.")

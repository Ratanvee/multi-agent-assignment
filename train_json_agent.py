import os
import joblib
import json
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

# Sample JSON strings
json_samples = [
    '{"name": "Lovepreet", "email": "lovepreet@example.com", "age": 25}',             # user_profile
    '{"order_id": 123, "item": "Book", "quantity": 2, "price": 500}',         # order_info
    '{"product_id": "P01", "name": "Shoes", "price": 1200, "stock": 10}',     # product_details
    '{"user": "Bob", "feedback": "Great service", "rating": 5}',              # feedback
    '{"lat": 28.7041, "lon": 77.1025, "timestamp": "2023-10-01T12:00:00"}'    # location_data
]

labels = [
    "user_profile",
    "order_info",
    "product_details",
    "feedback",
    "location_data"
]

# Ensure models folder exists
os.makedirs("models", exist_ok=True)

# Train a text-based classifier
pipeline = Pipeline([
    ("tfidf", TfidfVectorizer()),
    ("clf", LogisticRegression())
])

pipeline.fit(json_samples, labels)

# Save the model
joblib.dump(pipeline, "models/json_type_model.pkl")
print("JSON type classification model saved.")

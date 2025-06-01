import os
import joblib
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

# Sample document content and labels
texts = [
    "Dear John, this letter is to inform you about...",               # letter
    "This is to certify that Mr. Sharma has completed...",           # certificate
    "Meeting Agenda: 1. Budget 2. Timeline 3. Review",               # meeting_agenda
    "Resume of Ratan\nSkills: Python, ML, Flask...",                 # resume
    "Invoice Number: #12345\nTotal: 5500 INR"                        # invoice
]

labels = [
    "letter",
    "certificate",
    "meeting_agenda",
    "resume",
    "invoice"
]

# Ensure models folder exists
os.makedirs("models", exist_ok=True)

# Train pipeline
pipeline = Pipeline([
    ("tfidf", TfidfVectorizer()),
    ("clf", LogisticRegression())
])

pipeline.fit(texts, labels)

# Save model
joblib.dump(pipeline, "models/document_type_model.pkl")
print("Document classification model saved.")

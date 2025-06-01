import joblib

# Load trained models
intent_model = joblib.load("models/email_intent_model.pkl")
urgency_model = joblib.load("models/email_urgency_model.pkl")

def process_email(content, memory):
    """
    Process email using AI model to classify intent and urgency.
    
    Args:
        content (str): Raw email text.
        memory: Shared memory (not deeply used here).
    
    Returns:
        dict: Result with AI predictions.
    """
    # Extract sender
    sender = "Unknown"
    lines = content.splitlines()
    for line in lines:
        if line.lower().startswith("from:"):
            sender = line.split(":", 1)[1].strip()
            break

    # Predict intent and urgency
    intent = intent_model.predict([content])[0]
    urgency = urgency_model.predict([content])[0]

    # Extract summary (first 3 non-empty lines)
    summary = [line.strip() for line in lines if line.strip()][:3]

    return {
        "status": "Processed",
        "sender": sender,
        "predicted_intent": intent,
        "predicted_urgency": urgency,
        "summary": summary
    }


# process_email(costomer_complaint, memory=None)
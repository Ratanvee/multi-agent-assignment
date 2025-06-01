import json
import joblib

# Load ML model
json_model = joblib.load("models/json_type_model.pkl")

def process_json(json_string, memory):
    """
    Analyze a JSON string and predict the type of data it represents.
    
    Args:
        json_string (str): Input JSON string.
        memory (dict): Shared memory (not used deeply here).
    
    Returns:
        dict: Status, classification, keys, values summary
    """
    try:
        data = json.loads(json_string)
    except json.JSONDecodeError:
        return {
            "status": "Failed",
            "reason": "Invalid JSON format"
        }

    # Predict the type using the model
    predicted_type = json_model.predict([json_string])[0]

    # Extract summary
    keys = list(data.keys())
    values = [str(data[k]) for k in keys][:3]

    return {
        "status": "Processed",
        "predicted_type": predicted_type,
        "keys": keys,
        "sample_values": values
    }

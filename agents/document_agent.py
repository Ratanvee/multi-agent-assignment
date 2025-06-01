import os
import PyPDF2
import docx
import joblib

# Load the trained ML model
doc_model = joblib.load("models/document_type_model.pkl")

def extract_text_from_pdf(file_path):
    try:
        with open(file_path, 'rb') as f:
            reader = PyPDF2.PdfReader(f)
            text = ''
            for page in reader.pages:
                text += page.extract_text() or ''
            return text
    except Exception as e:
        return str(e)

def extract_text_from_docx(file_path):
    try:
        doc = docx.Document(file_path)
        return '\n'.join([para.text for para in doc.paragraphs])
    except Exception as e:
        return str(e)

def extract_text(file_path):
    ext = os.path.splitext(file_path)[1].lower()
    if ext == ".pdf":
        return extract_text_from_pdf(file_path)
    elif ext == ".docx":
        return extract_text_from_docx(file_path)
    elif ext == ".txt":
        with open(file_path, 'r', encoding='utf-8') as f:
            return f.read()
    else:
        return None

def process_document(file_path, memory):
    text = extract_text(file_path)
    if not text:
        return {
            "status": "Failed",
            "reason": "Unsupported file type or empty content"
        }
    
    predicted_type = doc_model.predict([text])[0]

    return {
        "status": "Processed",
        "predicted_type": predicted_type,
        "sample_text": text
    }

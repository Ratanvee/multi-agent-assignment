#  Multi-Agent AI Processing System

This project is a Python-based system that uses multiple intelligent agents to process different types of data files like:

-  Emails
-  JSON files
-  Documents (.txt, .pdf, .docx)

Each file type is handled by its own "agent" using AI/ML or basic data processing. The system stores results in a shared memory database (SQLite).

---

##  Project Structure
    multi-agent-model/
      agents/
        email_agent.py # AI-based intent detection from emails
        json_agent.py # Extract fields from JSON files
        document_agent.py # Process txt/pdf/docx files

      main.py # Main runner to process all files
      train_email_agent.py # Trains ML model for email intent
      train_document_agent.py # Trains ML model for documents(.pdf, .docx, .word, .txt, etc.) intent
      train_json_agent.py # Trains ML model for json intent
      
      documents/ # Input files for document agent
      models/ # Saved email intent ML model
      myenv/  # To make virtual environement 
      memory.db # SQLite memory storage
      README.md # Project overview and instructions


---

##  How It Works

1. **Emails**: Classified into categories like complaint, inquiry using ML model  
2. **JSON**: Fields like `order_id`, `item`, `price` are extracted  
3. **Documents**: Text content is read and summarized  

Each result is saved in a **SQLite memory** table.


##  How to Run

1. Install requirements:
   pip install -r requirements.txt

2. Train the ML model:
   python train_document_agent.py
   python train_email_agent.py
   python train_json_agent.py

3. Run the main program:
   python main.py

 ## Memory Storage (SQLite)
   Results are stored in a local database (memory.db) using this table:

    CREATE TABLE memory (
      key TEXT PRIMARY KEY,
      value TEXT
    );


---

## Example Output
    Email Agent Result:
    intent: complaint
    
    JSON Agent Result:
    order_id: 101
    item: Keyboard
    price: 899
    
    Document Agent Result:
    summary: Customer requests a refund due to damaged product.


---

## Features
  - Easy-to-extend agent architecture
  - AI/ML-based classification for emails
  - NLP for documents
  - SQLite-based memory system

---

## Author
  Ratanveer Singh    <br>+91 9056318551 <br>     ratanveers420@gmail.com <br><br>
  AI/ML Developer

import os
import sqlite3
from agents.email_agent import process_email
from agents.json_agent import process_json
from agents.document_agent import process_document

# Initialize SQLite-based memory
def init_db():
    conn = sqlite3.connect("memory.db")
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS memory (
            key TEXT PRIMARY KEY,
            value TEXT
        )
    ''')
    conn.commit()
    return conn, c

def get_memory(conn, key):
    c = conn.cursor()
    c.execute("SELECT value FROM memory WHERE key = ?", (key,))
    row = c.fetchone()
    return row[0] if row else None

import json

def set_memory(conn, key, value):
    c = conn.cursor()
    # Convert value to JSON string if it's not already a string
    if not isinstance(value, str):
        value = json.dumps(value)
    c.execute("REPLACE INTO memory (key, value) VALUES (?, ?)", (key, value))
    conn.commit()


# Start memory database
conn, cursor = init_db()

# Shared memory dictionary (you can load memory as needed)
memory = {}

# EMAIL AGENT
sample_email = """
From: ratan@email.com

Hi,

I need help with my recent order. The item arrived broken and I need a replacement ASAP.

Regards,
Customer
"""

result = process_email(sample_email, memory)

# Save and display result
for k, v in result.items():
    set_memory(conn, f"email:{k}", v)

print("Email Agent Result:")
for k, v in result.items():
    print(f"{k}: {v}")

print("\n\n\n<-------------------------------------------------------------------------------------------------------------------->\n")

# JSON AGENT
sample_json = '''
{
    "order_id": 456,
    "item": "Keyboard",
    "quantity": 1,
    "price": 999
}
'''

result = process_json(sample_json, memory={})
for k, v in result.items():
    set_memory(conn, f"json:{k}", str(v))

print("JSON Agent Result:")
for k, v in result.items():
    print(f"{k}: {v}")

print("\n\n\n<-------------------------------------------------------------------------------------------------------------------->\n")

# DOCUMENT AGENT
documents_dir = "documents"
for filename in os.listdir(documents_dir):
    file_path = os.path.join(documents_dir, filename)

    if not os.path.isfile(file_path) or filename.startswith('.'):
        continue

    print("\n<-------------------------------------------------------------------------------------------------------------------->\n")
    print(f"Processing File: {filename}\n")
    result = process_document(file_path, memory)

    # Save memory per file
    for k, v in result.items():
        set_memory(conn, f"doc:{filename}:{k}", str(v))

    print("Document Agent Result:")
    for k, v in result.items():
        print(f"{k}: {v}")

# Close SQLite connection
conn.close()

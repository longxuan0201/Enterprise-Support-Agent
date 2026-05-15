import requests

# test ingest
url_ingest = "http://127.0.0.1:8000/ingest"
with open("data/sample_sop.txt", "r", encoding="utf-8") as f:
    content = f.read()
    
payload = {
    "title": "SAP Interface Failure Initial Troubleshooting SOP",
    "content": content,
    "source_type": "sop",
    "system_name": "SAP",
    "environment": "production",
    "tags": ["sap", "interface", "troubleshooting", "sop"]
}   


response = requests.post(url_ingest, json=payload)
print(response.status_code)
print(response.text)

# test retrieve
url_retrieve = "http://127.0.0.1:8000/retrieve"
payload_retrieve = {
    "query": "What is the SAP interface failure initial troubleshooting SOP?",
    "top_k": 2
}

response = requests.post(url_retrieve, json=payload_retrieve)
print(response.status_code)
print(response.text)

# test chat
url_chat = "http://127.0.0.1:8000/chat"
payload_chat = {
    "question": "What is the SAP interface failure initial troubleshooting SOP?",
}

response = requests.post(url_chat, json=payload_chat)
print(response.status_code)
print(response.text)
import requests



url = "http://127.0.0.1:8000/ingest"
with open("data\sample_sop.txt", "r", encoding="utf-8") as f:
    content = f.read()
    
payload = {
    "title": "SAP Interface Failure Initial Troubleshooting SOP",
    "content": content,
    "source_type": "sop",
    "system_name": "Enterprise Support Agent",
    "environment": "production",
    "tags": ["sap", "interface", "troubleshooting", "sop"]
}   


response = requests.post(url, json=payload)
print(response.status_code)
print(response.text)

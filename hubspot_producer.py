import requests
import os
import json
from dotenv import load_dotenv
from kafka import KafkaProducer

load_dotenv()

ACCESS_TOKEN = os.getenv("HUBSPOT_ACCESS_TOKEN")

producer = KafkaProducer(
    bootstrap_servers="localhost:9092",
    value_serializer=lambda v: json.dumps(v).encode("utf-8")
)

url = "https://api.hubapi.com/crm/v3/objects/contacts"

headers = {
    "Authorization": f"Bearer {ACCESS_TOKEN}"
}

response = requests.get(url, headers=headers)

data = response.json()

contacts = data["results"]

for contact in contacts:

    record = {
        "id": contact.get("id"),
        "firstname": contact["properties"].get("firstname"),
        "lastname": contact["properties"].get("lastname"),
        "email": contact["properties"].get("email")
    }

    producer.send(
        "crm_contacts",
        value=record
    )

    print(f"Sent : {record}")

producer.flush()

print("All HubSpot Contacts Sent Successfully")
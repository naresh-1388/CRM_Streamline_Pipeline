import requests
from dotenv import load_dotenv
import os
import json

load_dotenv()

ACCESS_TOKEN = os.getenv("HUBSPOT_ACCESS_TOKEN")

url = "https://api.hubapi.com/crm/v3/objects/contacts"

headers = {
    "Authorization": f"Bearer {ACCESS_TOKEN}"
}

response = requests.get(url, headers=headers)

data = response.json()

with open("contacts.json", "w") as file:
    json.dump(data, file, indent=4)

print("JSON File Created Successfully")
from kafka import KafkaConsumer
import json

consumer = KafkaConsumer(
    "crm_contacts",
    bootstrap_servers="localhost:9092",
    auto_offset_reset="latest",
    value_deserializer=lambda x: json.loads(x.decode("utf-8"))
)
print("Listening For HubSpot Contacts...")

with open("contacts.json", "a") as file:

    for message in consumer:

        contact = message.value

        json.dump(contact, file)

        file.write("\n")

        file.flush()

        print(f"Saved : {contact}")
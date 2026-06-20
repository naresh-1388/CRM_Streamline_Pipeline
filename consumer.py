from kafka import KafkaConsumer
import json

consumer = KafkaConsumer(
    "crm_contacts",
    bootstrap_servers="localhost:9092",
    auto_offset_reset="earliest",
    value_deserializer=lambda x: json.loads(x.decode("utf-8"))
)

print("Waiting For Messages...")

for message in consumer:
    print(message.value)
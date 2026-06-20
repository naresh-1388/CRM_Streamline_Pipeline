from kafka import KafkaProducer
import json

producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

data = {
    "id": 102,
    "name": "Gopinath",
    "skill": "Kafka"
}

producer.send("crm_contacts", value=data)

producer.flush()

print("Message Sent Successfully")
from kafka import KafkaConsumer
import snowflake.connector
from dotenv import load_dotenv
import json
import os

load_dotenv()

consumer = KafkaConsumer(
    "crm_contacts",
    bootstrap_servers="localhost:9092",
    auto_offset_reset="latest",
    value_deserializer=lambda x: json.loads(x.decode("utf-8"))
)

conn = snowflake.connector.connect(
    user=os.getenv("SNOWFLAKE_USER"),
    password=os.getenv("SNOWFLAKE_PASSWORD"),
    account=os.getenv("SNOWFLAKE_ACCOUNT"),
    warehouse=os.getenv("SNOWFLAKE_WAREHOUSE"),
    database=os.getenv("SNOWFLAKE_DATABASE"),
    schema=os.getenv("SNOWFLAKE_SCHEMA")
)

cursor = conn.cursor()

print("Listening For Kafka Messages...")

for message in consumer:

    contact = message.value

    cursor.execute(
        """
        INSERT INTO RAW_CONTACTS
        (ID,FIRSTNAME,LASTNAME,EMAIL)
        VALUES (%s,%s,%s,%s)
        """,
        (
            contact.get("id"),
            contact.get("firstname"),
            contact.get("lastname"),
            contact.get("email")
        )
    )

    conn.commit()

    print(f"Inserted : {contact}")
# CRM Streamline Pipeline

## Project Overview

CRM Streamline Pipeline is an end-to-end Data Engineering project that extracts customer data from HubSpot CRM using REST APIs, streams the data through Apache Kafka, loads it into Snowflake, and transforms it using dbt for analytics and reporting.

This project demonstrates real-world Data Engineering concepts including API Integration, Event Streaming, Cloud Data Warehousing, Data Transformation, and Data Quality Testing.

---

## Architecture

```text
HubSpot CRM
      ↓
REST API
      ↓
Python
      ↓
Kafka Producer
      ↓
Kafka Topic
      ↓
Kafka Consumer
      ↓
Snowflake RAW_CONTACTS
      ↓
dbt STG_CONTACTS
      ↓
dbt DIM_CUSTOMERS
      ↓
dbt CUSTOMER_SUMMARY
      ↓
Power BI
```

---

## Technologies Used

* HubSpot CRM
* Python
* REST API
* Apache Kafka
* Docker
* Snowflake
* dbt (Data Build Tool)
* Power BI
* Git
* GitHub

---

## Business Problem

Organizations store customer information in CRM platforms such as HubSpot. Data Engineers need to ingest this data, process it, store it in a data warehouse, and transform it into analytics-ready datasets for reporting and business insights.

This project simulates a real-world CRM data pipeline.

---

## Project Workflow

### Step 1: HubSpot CRM Setup

* Created HubSpot account
* Imported sample customer records
* Created Private App
* Generated Access Token
* Configured API scopes

### Step 2: API Data Extraction

Python was used to call HubSpot Contacts API.

Endpoint:

```text
/crm/v3/objects/contacts
```

Customer records were extracted in JSON format.

### Step 3: Kafka Setup

* Installed Docker Desktop
* Configured WSL2 and Ubuntu
* Created Kafka Broker using Docker Compose
* Exposed Kafka on Port 9092

### Step 4: Kafka Producer

Developed a Kafka Producer that publishes customer records to the Kafka topic.

Topic Name:

```text
crm_contacts
```

### Step 5: Kafka Consumer

Developed Kafka Consumer that subscribes to the topic and receives customer events.

### Step 6: Snowflake Integration

Created Snowflake database:

```text
CRM_STREAMLINE_DB
```

Created schema:

```text
RAW
```

Created raw ingestion table:

```sql
CREATE TABLE RAW_CONTACTS
(
    ID STRING,
    FIRSTNAME STRING,
    LASTNAME STRING,
    EMAIL STRING
);
```

Consumer inserts customer records directly into Snowflake.

### Step 7: dbt Transformations

Created the following dbt models:

#### stg_contacts

Staging model built on top of RAW_CONTACTS.

#### dim_customers

Business-friendly customer dimension model.

#### customer_summary

Aggregated model used for reporting.

---

## dbt Lineage

```text
RAW_CONTACTS
      ↓
STG_CONTACTS
      ↓
DIM_CUSTOMERS
      ↓
CUSTOMER_SUMMARY
```

---

## Data Quality Testing

Implemented dbt tests:

### CUSTOMER_ID

* unique
* not_null

### EMAIL

* not_null

All tests passed successfully.

```text
PASS=3
WARN=0
ERROR=0
```

---

## Snowflake Objects Created

### Database

```text
CRM_STREAMLINE_DB
```

### Schema

```text
RAW
```

### Tables

```text
RAW_CONTACTS
STG_CONTACTS
DIM_CUSTOMERS
CUSTOMER_SUMMARY
```

---

## Project Structure

```text
CRM_Streamline_Pipeline
│
├── producer.py
├── consumer.py
├── hubspot_producer.py
├── hubspot_consumer.py
├── snowflake_consumer.py
├── test_api.py
├── requirements.txt
│
├── kafka
│   └── docker-compose.yml
│
└── crm_streamline_dbt
    │
    ├── dbt_project.yml
    │
    └── models
        ├── stg_contacts.sql
        ├── dim_customers.sql
        ├── customer_summary.sql
        └── schema.yml
```

---

## Key Concepts Demonstrated

* REST API Integration
* JSON Processing
* Apache Kafka Streaming
* Producer and Consumer Architecture
* Docker Containerization
* Snowflake Data Warehousing
* dbt Transformations
* Data Quality Testing
* Dimensional Modeling
* Git Version Control

---

## Results

Successfully built a complete CRM Data Pipeline that:

* Extracts customer data from HubSpot CRM
* Streams events using Apache Kafka
* Loads records into Snowflake
* Transforms data using dbt
* Validates data quality using dbt tests
* Produces analytics-ready datasets

---

## Future Enhancements

* HubSpot Companies API Integration
* HubSpot Deals API Integration
* Star Schema Implementation
* Fact Tables and Dimension Tables
* Incremental dbt Models
* Kafka Monitoring
* Airflow Orchestration
* Power BI Dashboard

---

## Resume Description

Built an end-to-end CRM data pipeline using HubSpot CRM, Python, Apache Kafka, Snowflake and dbt. Extracted customer records through REST APIs, streamed data through Kafka topics using Producers and Consumers, loaded records into Snowflake raw tables, transformed data using dbt models and implemented data quality tests to create analytics-ready datasets.

# Smart Home Energy Optimizer — IoT System Design

Team 2 – AAI 530: Data Analytics and the Internet of Things  
Project: Smart Home Energy Optimization Using UK‑DALE

---

## 1. System Overview

Our Smart Home Energy Optimizer is a conceptual IoT system designed to monitor electricity usage at both the whole‑home and appliance levels. The goal is to take raw sensor data, process it efficiently, and generate insights that help homeowners and utilities better understand and manage energy consumption.

The system is built around a few core ideas:

- Collect real‑time power data from smart meters and appliance‑level sensors  
- Perform lightweight processing on an in‑home edge device  
- Stream data to the cloud for storage, analytics, and machine learning  
- Support two ML tasks:
  - CNN‑based NILM for appliance disaggregation  
  - LSTM/GRU‑based forecasting for next‑hour energy usage  
- Scale cleanly from a single home to thousands of households  

This design mirrors what a real smart‑home energy platform might look like, while staying grounded in the UK‑DALE dataset we’re using for the project.

---

## 2. Sensors and Data Sources

### Sensor Types

**Smart meter (mains)**  
- Measures whole‑home active power at 1–6 second intervals  
- Installed at the main electrical panel  

**Appliance‑level meters (sub‑meters)**  
- Plug‑level or circuit‑level sensors for major appliances  
- Provide ground‑truth labels for NILM model training  

### Deployment Considerations

- Smart meter: utility interface or main panel  
- Sub‑meters: high‑impact appliances (kitchen, laundry, HVAC, etc.)  

### Limitations

- Sampling frequency varies by device  
- Wireless meters may drop packets  
- Not all appliances are sub‑metered, so NILM must generalize  

---

## 3. Edge Processing

### Edge Device

We assume a small, low‑power gateway device (e.g., Raspberry Pi‑class hardware) inside the home. It connects to meters using Zigbee, Z‑Wave, Wi‑Fi, or wired protocols.

### Responsibilities at the Edge

**Data collection and buffering**  
- Subscribes to or polls meter readings  
- Buffers data during outages  

**Lightweight preprocessing**  
- Normalizes timestamps  
- Removes invalid readings  
- Optionally downsamples to 1‑minute intervals  

**Local analytics (optional)**  
- Simple threshold‑based alerts  
- Basic fallback logic if the cloud is unreachable  

### Resource Requirements

- Minimal CPU and memory  
- Enough storage to buffer several hours of data  
- Low power consumption for 24/7 operation  

---

## 4. Networking and Communication

### Connectivity

- Primary: home broadband  
- Optional: cellular backup  

### Messaging Protocol

**MQTT (recommended)**  
- Lightweight and ideal for IoT  
- Topics such as:
  - `house/{house_id}/mains`  
  - `house/{house_id}/appliance/{appliance_id}`  

**Alternative:** HTTPS/REST for batch uploads  

### Security

- TLS encryption  
- Per‑household authentication  
- Topic‑level authorization  

---

## 5. Cloud Ingestion, Storage, and Processing

### 5.1 Ingestion Layer

**MQTT broker or IoT hub**  
- Handles thousands of connections  
- Manages retries and QoS  

**Stream processing**  
- Kafka consumer, serverless function, or similar  
- Validates and enriches messages  
- Routes data to storage and ML pipelines  

### 5.2 Storage Layer

**Time‑series storage**  
- Stores resampled mains and appliance data  
- Partitioned by `house_id` and time window  
- Supports EDA, training, and dashboards  

**Object storage (data lake)**  
- Stores raw or lightly processed data  
- Used for offline training and archival  

**Metadata store**  
- Tracks household attributes, appliance mappings, and model versions  

---

## 6. Machine Learning Inference Pipeline

The system supports two ML tasks:

1. **CNN for NILM**  
2. **LSTM/GRU for forecasting**  

### 6.1 Feature Preparation

**For NILM (CNN)**  
- Sliding windows of 1‑minute mains power  
- Labels from sub‑meters  
- Normalization, windowing, optional augmentation  

**For forecasting (LSTM/GRU)**  
- Historical mains power (e.g., past 24 hours)  
- Optional features: time of day, day of week, seasonality  
- Target: next‑hour consumption  

### 6.2 Inference Architecture

**Batch inference**  
- Runs every 15–60 minutes  
- Writes predictions to a dedicated table  

**Streaming inference (optional)**  
- Processes data as it arrives  
- Useful for real‑time alerts  

### 6.3 Edge vs. Cloud Inference

**Cloud inference (default)**  
- Easier to update and scale  

**Edge inference (optional)**  
- Lower latency  
- Useful for simple NILM or alerts  

---

## 7. Scalability to Many Households

A major design goal is to ensure the system can scale from one home to thousands.

### Key Strategies

**Partitioning by household**  
- All data is partitioned by `house_id`  
- Enables parallel processing  

**Horizontally scalable ingestion**  
- MQTT brokers and stream processors can scale out  

**Storage scalability**  
- Time‑series and object storage support sharding and compression  

**Model serving at scale**  
- Containerized or serverless workloads  
- Autoscaling and versioning  

**Multi‑tenant dashboard**  
- Users see only their own data  
- Utilities can view aggregated insights  

---

## 8. Dashboard Integration

The dashboard connects to curated tables containing both raw and ML‑generated insights.

### Core Visualizations

1. **Status visualization**  
   - Current mains power or next‑hour forecast  

2. **Summary visualization**  
   - Daily or weekly usage trends  

3. **NILM insight**  
   - Appliance‑level energy breakdown  

4. **Forecasting insight**  
   - Predicted vs. actual next‑hour usage  

---

## 9. Summary

This system design outlines a realistic, scalable IoT architecture for smart home energy optimization using the UK‑DALE dataset. It brings together sensors, edge processing, cloud infrastructure, and two complementary ML models to create a complete end‑to‑end solution. In the context of AAI‑530, this design forms the backbone of our final project and ties together the dataset, ML models, and dashboard into a cohesive application.

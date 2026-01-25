# Smart Home Energy Optimizer
### Team 2 – AAI 530: Data Analytics and the Internet of Things  
Greg Bauer • Andrea Thomas • Darius Rowser  
University of San Diego  
Final Project – Spring 2026

---

## 📘 Project Overview
This project develops a smart home energy optimization system using the United Kingdom Domestic Appliance‑Level Electricity (UK‑DALE) dataset. The system integrates an Internet of Things (IoT) architecture, machine learning (ML) models, and a Tableau dashboard to provide actionable insights into residential energy consumption.

Our goals:
- Design a complete IoT system architecture for scalable multi‑household deployment  
- Perform exploratory data analysis (EDA) and preprocessing  
- Train two ML models:
  - A Convolutional Neural Network (CNN) for Non‑Intrusive Load Monitoring (NILM)
  - A Long Short‑Term Memory (LSTM) model for next‑hour energy forecasting
- Build a Tableau dashboard with status, summary, and ML insight visualizations

---

## 📂 Repository Structure
- `data/` — raw, interim, and processed datasets  
- `notebooks/` — EDA, preprocessing, CNN, LSTM, dashboard exports  
- `src/` — modular Python code for data processing and model training  
- `docs/` — IoT system design, ML descriptions, APA report drafts  
- `dashboard/` — Tableau assets  
- `reports/` — final report and status updates  

---

## 📊 Dataset
**United Kingdom Domestic Appliance‑Level Electricity (UK‑DALE)**  
Kelly & Knottenbelt (2015), Scientific Data  
https://www.nature.com/articles/sdata20157

https://ukerc.rl.ac.uk/cgi-bin/dataDiscover.pl?Action=detail&dataid=7d78f943-f9fe-413b-af52-1816f9d968b0

https://jack-kelly.com/data/

---

## 🧠 Machine Learning Models
- **CNN for NILM** (built from scratch, no pre‑trained models)  
- **LSTM/GRU forecasting model** for next‑hour energy prediction  

---

## 🏗️ IoT System Design
Includes:
- Sensors  
- Edge processing  
- Networking  
- Cloud ingestion  
- Storage and scalability  
- ML inference pipeline  

See `/docs/iot_system_design/`.

---

## 📜 License
Academic use only.

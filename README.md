---

# **README.md — Smart Home Energy Optimizer**  
### Team 2 — AAI 530: Data Analytics & the Internet of Things  
**Greg Bauer • Andrea Thomas • Darius Rowser**  
University of San Diego — Spring 2026

---

## **📘 Project Overview**

This repository contains a complete IoT‑to‑machine‑learning pipeline for smart home energy analytics using the **UK‑DALE** dataset. The system integrates:

- A scalable **IoT architecture** for multi‑household ingestion  
- **Exploratory data analysis (EDA)** and preprocessing workflows  
- A **CNN‑based NILM classifier** for appliance‑level event detection  
- A **minute‑level and hourly LSTM forecasting pipeline**  
- A **Tableau dashboard** for real‑time and historical visualization  

The project demonstrates how IoT sensing, cloud processing, and deep learning can be combined to generate actionable insights for residential energy optimization.

---

## **📂 Repository Structure**

```
smart-home-energy-optimizer/
│
├── Project Structure.md
├── README.md
├── Darius_CNN_Training_Loop.ipynb
│
├── dashboard/
│   └── tableau_exports/
│
├── data/
│   ├── House_1_kettle_analysis.csv
│   ├── House_1_kettle_analysis - House_1_kettle_analysis (1).csv
│   ├── House_2_kettle_analysis.csv
│   ├── House_2_kettle_analysis - House_2_kettle_analysis (1).csv
│   ├── inputs.gitkeep
│   │
│   ├── interim/
│   │   ├── House_1_cleaned.csv
│   │   └── House_2_cleaned.csv
│   │
│   ├── processed/
│   │   └── (future processed outputs)
│   │
│   └── raw/
│       ├── ukdale.h5
│       ├── archive/
│       ├── house_1/
│       ├── house_2/
│       ├── house_3/
│       ├── house_4/
│       ├── house_5/
│       └── metadata/
│
├── docs/
│   ├── HDF5_hierarchy_diagram.md
│   ├── data_dictionary.md
│   ├── dataset_selection.md
│   ├── how_to_run_ingestion.md
│   └── iot_system_design/
│       └── iot_system_diagram.md
│
├── notebooks/
│   ├── 00_explore_ukdale_h5.ipynb
│   ├── 01_data_ingest_from_hd5.ipynb
│   ├── 01_eda.ipynb
│   ├── Darius_CNN_Training_Loop.ipynb
│   ├── Darius_NILM_CNN_Training.ipynb
│   ├── EDA_Houses_1_and_2.ipynb
│   ├── IoT_Group_Project_Data_Cleaning.ipynb
│   ├── LSTM complex hourly model.ipynb
│   ├── LSTM model comparison of simple vs complex.ipynb
│   ├── LSTM simple hourly model.ipynb
│   ├── LSTM simple minute model.ipynb
│   ├── Team2_CNN_NILM_Clean_Final DR.ipynb
│   ├── model_lstm_hourly_forecast_house1.ipynb
│   ├── Untitled.ipynb
│   └── Untitled1.ipynb
│
├── reports/
│   └── status_reports/
│       ├── Week_1.md
│       ├── cnn_house2_to_house1_kettle_on_thr189_anyOn.keras
│       ├── cnn_house2_to_house1_kettle_on_thr189_anyOn_config.json
│       └── cnn_house2_to_house1_tableau_datasheet.csv
│
├── src/
│   ├── __init__.py
│   ├── config.py
│   ├── data_download.py
│   ├── data_ingest.py
│   ├── pipeline.py
│   ├── requirements.txt
│   │
│   ├── data/
│   │   ├── interim/
│   │   │   ├── House_1_cleaned.csv
│   │   │   ├── House_1_kettle_analysis.csv
│   │   │   ├── House_2_cleaned.csv
│   │   │   └── House_2_kettle_analysis.csv
│   │   │
│   │   ├── processed/
│   │   │   └── building1_mains_kettle_1min_180d.csv
│   │   │
│   │   └── reports/
│   │       ├── cnn_kettle_house1_eval.txt
│   │       ├── lstm_first_24h.png
│   │       ├── lstm_loss_curve.png
│   │       ├── lstm_residuals.png
│   │       └── lstm_window.png
│   │
│   └── models/
│       ├── cnn_nilm.py
│       ├── lstm_forecast.py
│       ├── cnn_kettle_house2.keras
│       ├── cnn_kettle_scaler_house2.pkl
│       ├── lstm_house1_forecast.keras
│       └── lstm_scaler_house1.pkl
│
└── models/
    ├── requirements.txt
    └── (trained model artifacts)
```

---

## **🧠 Machine Learning Models**

### **🔌 CNN NILM Classifier (`src/models/cnn_nilm.py`)**
- Detects kettle activation events from aggregate mains power  
- Window‑based framing (default: 24 timesteps)  
- Binary label computed from `kettle_watts` threshold  
- Trains on House 2 → evaluates on House 1  
- Outputs:
  - `cnn_kettle_house2.keras`
  - `cnn_kettle_scaler_house2.pkl`
  - `cnn_kettle_house1_eval.txt`

### **📈 LSTM Forecasting Model (`src/models/lstm_forecast.py`)**
- Legacy hourly forecaster (168‑hour lookback)  
- Predicts next‑hour aggregate mains power  
- Resamples to `"1h"`  
- Outputs:
  - `lstm_house1_forecast.keras`
  - `lstm_scaler_house1.pkl`

### **⚙️ Pipeline Orchestrator (`src/pipeline.py`)**
Supports three modes:

| Mode        | Description |
|-------------|-------------|
| `full`      | Run CNN NILM + LSTM forecasting |
| `cnn_only`  | Run CNN NILM only |
| `lstm_only` | Run LSTM forecasting only |

Usage:

```bash
python -m src.pipeline --mode full
```

---

## **📊 Dataset**

**UK‑DALE: UK Domestic Appliance‑Level Electricity Dataset**  
Kelly & Knottenbelt (2015), *Scientific Data*

---

## **🏗️ IoT System Design**

Documentation located in:

```
docs/iot_system_design/
```

Includes:

- System architecture diagram  
- Ingestion workflow  
- Storage layers  
- ML pipeline integration  

---

## **📊 Dashboard**

Tableau dashboards include:

- Real‑time status visualization  
- Daily/weekly consumption summaries  
- CNN NILM probability traces + confusion matrix  
- LSTM predicted vs. actual consumption  

---

## **🚀 Getting Started**

### Install dependencies
```
pip install -r src/requirements.txt
```

### Run pipeline
```
python -m src.pipeline --mode full
```

### Explore notebooks
Open any notebook in `/notebooks/`.

---

## **📜 License**
Academic use only.

---
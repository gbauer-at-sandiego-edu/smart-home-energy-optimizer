---

```markdown
# Project Structure

This repository is organized to support the full end‑to‑end workflow for the **Smart Home Energy Optimizer** project, including data ingestion, preprocessing, exploratory analysis, modeling, documentation, and reporting. The structure below reflects the current state of the repository.

```

smart-home-energy-optimizer/

│  
├── README.md  
├── .gitignore  
├── environment.yml  
│  
├── data/  
│   ├── raw/  
│   ├── interim/  
│   └── processed/  
│  
├── notebooks/  
│   ├── 01_eda.ipynb  
│   ├── EDA_Houses_1_and_2.ipynb  
│   ├── IoT_Group_Project_Data_Cleaning.ipynb  
│   ├── Darius_CNN_Training_Loop.ipynb  
│   ├── Darius_NILM_CNN_Training.ipynb  
│   └── LSTM_house1_training.ipynb  
│  
├── src/  
│   ├── config.py  
│   ├── data_download.py  
│   ├── data_ingest.py  
│   └── (future) preprocessing, model, training, evaluation modules  
│  
├── docs/  
│   └── iot_system_design/  
│       ├── CNN_vs_LSTM_Justification.md  
│       ├── scalability_considerations.md  
│       ├── system_desing.md  
│       ├── data_dictionary.md  
│       ├── dataset_selection.md  
│       └── how_to_run_ingestion.md  
│  
├── reports/  
│   └── status_reports/  
│       └── Week_1.md  
│  
└── Project Structure.md

```

## Folder Descriptions

### `data/`
Contains all dataset files in three stages:

- **raw/** – original downloaded data  
- **interim/** – partially cleaned or transformed data  
- **processed/** – final modeling‑ready datasets  

### `notebooks/`
Jupyter notebooks for exploratory data analysis, data cleaning, and model experimentation:

- EDA across houses  
- Cleaning and resampling  
- CNN training loop prototype  
- NILM CNN training  
- LSTM forecasting  

### `src/`
Python source code for ingestion and configuration:

- `config.py` – configuration settings  
- `data_download.py` – dataset download logic  
- `data_ingest.py` – ingestion and resampling pipeline  
- *(Planned additions)* preprocessing, model definition, training, and evaluation modules  

### `docs/iot_system_design/`
Documentation for system architecture and Week 1 deliverables:

- CNN vs. LSTM justification  
- Scalability considerations  
- System design document  
- Data dictionary  
- Dataset selection  
- Ingestion instructions  

### `reports/status_reports/`
Weekly project status reports.

---
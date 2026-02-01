```markdown

\# Project Structure



This repository is organized to support the full end‑to‑end workflow for the Smart Home Energy Optimizer project, including data ingestion, preprocessing, exploratory analysis, documentation, and reporting. The structure below reflects the current state of the repository.



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

│   ├── 01\_eda.ipynb

│   └── IoT\_Group\_Project\_Data\_Cleaning.ipynb

│

├── src/

│   ├── config.py

│   ├── data\_download.py

│   └── data\_ingest.py

│

├── docs/

│   ├── iot\_system\_design/

│   │   ├── CNN\_vs\_LSTM\_Justification.md

│   │   ├── scalability\_considerations.md

│   │   ├── system\_desing.md

│   │   ├── data\_dictionary.md

│   │   ├── dataset\_selection.md

│   │   └── how\_to\_run\_ingestion.md

│

├── reports/

│   └── status\_reports/

│       └── Week\_1.md

│

└── Project Structure.md

```



\## Folder Descriptions



\### `data/`

Contains all dataset files in three stages:

\- \*\*raw/\*\* – original downloaded data  

\- \*\*interim/\*\* – partially cleaned or transformed data  

\- \*\*processed/\*\* – final modeling‑ready datasets  



\### `notebooks/`

Jupyter notebooks for exploratory data analysis and data cleaning.



\### `src/`

Python source code for ingestion and configuration:

\- `config.py` – configuration settings  

\- `data\_download.py` – dataset download logic  

\- `data\_ingest.py` – ingestion and resampling pipeline  



\### `docs/iot\_system\_design/`

Documentation for system architecture and Week 1 deliverables:

\- CNN vs. LSTM justification  

\- Scalability considerations  

\- System design document  

\- Data dictionary  

\- Dataset selection  

\- Ingestion instructions  



\### `reports/status\_reports/`

Weekly project status reports.



---


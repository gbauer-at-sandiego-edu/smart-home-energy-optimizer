flowchart TD



&nbsp;   %% Top-level repo

&nbsp;   REPO\["smart-home-energy-optimizer (GitHub Repo)"]



&nbsp;   %% Directories

&nbsp;   REPO --> SRC\["src/"]

&nbsp;   REPO --> NOTE\["notebooks/"]

&nbsp;   REPO --> DOCS\["docs/"]

&nbsp;   REPO --> REPORTS\["reports/"]

&nbsp;   REPO --> DASH\["dashboard/"]

&nbsp;   REPO --> DATA\["data/"]

&nbsp;   REPO --> ENV\["environment.yml"]

&nbsp;   REPO --> README\["README.md"]



&nbsp;   %% src/

&nbsp;   subgraph SRC\_DIR\["src/ (Python Modules)"]

&nbsp;       INGEST\["data\_ingest.py"]

&nbsp;       DOWNLOAD\["data\_download.py"]

&nbsp;       CONFIG\["config.py"]

&nbsp;       MODELS\["models/"]

&nbsp;   end



&nbsp;   %% models/

&nbsp;   subgraph MODELS\_DIR\["models/ (Model Code)"]

&nbsp;       CNN\["cnn\_nilm.py"]

&nbsp;       LSTM\["lstm\_forecasting.py"]

&nbsp;       TRAIN\_UTILS\["train\_utils.py (planned)"]

&nbsp;   end



&nbsp;   %% notebooks/

&nbsp;   subgraph NOTE\_DIR\["notebooks/ (Jupyter Notebooks)"]

&nbsp;       EDA\["01\_eda.ipynb"]

&nbsp;       CLEAN\["02\_preprocessing.ipynb"]

&nbsp;       CNN\_NB\["03\_cnn\_nilm.ipynb"]

&nbsp;       LSTM\_NB\["04\_lstm\_forecasting.ipynb"]

&nbsp;       DASH\_NB\["05\_dashboard\_exports.ipynb"]

&nbsp;   end



&nbsp;   %% docs/

&nbsp;   subgraph DOCS\_DIR\["docs/ (Documentation)"]

&nbsp;       SYS\_DESIGN\["system\_design.md"]

&nbsp;       DATA\_SEL\["dataset\_selection.md"]

&nbsp;       DATA\_DICT\["data\_dictionary.md"]

&nbsp;       CNN\_LSTM\_JUST\["CNN\_vs\_LSTM\_Justification.md"]

&nbsp;       SCALABILITY\["scalability\_considerations.md"]

&nbsp;   end



&nbsp;   %% reports/

&nbsp;   subgraph REPORTS\_DIR\["reports/"]

&nbsp;       STATUS\["status\_reports/"]

&nbsp;       FINAL\["final\_report.pdf (planned)"]

&nbsp;   end



&nbsp;   %% dashboard/

&nbsp;   subgraph DASH\_DIR\["dashboard/"]

&nbsp;       TBL\_EXPORTS\["tableau\_exports/ (planned)"]

&nbsp;   end



&nbsp;   %% data/

&nbsp;   subgraph DATA\_DIR\["data/"]

&nbsp;       RAW\["raw/ (empty, .gitkeep)"]

&nbsp;       PROC\["processed/ (cleaned CSVs)"]

&nbsp;   end



&nbsp;   %% Relationships

&nbsp;   INGEST --> CONFIG

&nbsp;   INGEST --> PROC

&nbsp;   DOWNLOAD --> RAW

&nbsp;   CNN\_NB --> CNN

&nbsp;   LSTM\_NB --> LSTM

&nbsp;   EDA --> CLEAN

&nbsp;   CLEAN --> PROC

&nbsp;   CNN --> TRAIN\_UTILS

&nbsp;   LSTM --> TRAIN\_UTILS

&nbsp;   PROC --> CNN\_NB

&nbsp;   PROC --> LSTM\_NB

&nbsp;   PROC --> DASH\_NB




flowchart LR



&nbsp;   %% Code Pipeline

&nbsp;   subgraph CODE\["Code Pipeline (Backend + Dashboard)"]

&nbsp;       CODE\_COMMIT\["Commit to Repo<br/>Git Push"]

&nbsp;       CODE\_BUILD\["Build \& Unit Tests"]

&nbsp;       CODE\_SCAN\["Security Scan<br/>Lint • SAST"]

&nbsp;       CODE\_DEPLOY\["Deploy to Cloud<br/>Ingestion + Dashboard"]

&nbsp;   end



&nbsp;   %% Model Pipeline

&nbsp;   subgraph MODEL\["Model Pipeline (CNN + LSTM)"]

&nbsp;       DATA\_PULL\["Pull Curated Data<br/>TSDB + Object Storage"]

&nbsp;       TRAIN\["Train Models<br/>CNN NILM + LSTM Forecast"]

&nbsp;       EVAL\["Evaluate Models<br/>MAE • RMSE • F1"]

&nbsp;       REGISTRY\["Register Model<br/>Model Registry"]

&nbsp;       BATCH\_DEPLOY\["Deploy Batch Jobs<br/>Prediction Pipeline"]

&nbsp;   end



&nbsp;   %% Edge OTA Pipeline

&nbsp;   subgraph EDGE\["Edge OTA Pipeline"]

&nbsp;       EDGE\_COMMIT\["Commit Edge Code"]

&nbsp;       EDGE\_BUILD\["Build Edge Package"]

&nbsp;       EDGE\_SIGN\["Sign Firmware<br/>Integrity Check"]

&nbsp;       EDGE\_PUSH\["Push to OTA Server"]

&nbsp;       EDGE\_UPDATE\["Edge Auto‑Update<br/>Download + Apply"]

&nbsp;   end



&nbsp;   %% Connections

&nbsp;   CODE\_COMMIT --> CODE\_BUILD --> CODE\_SCAN --> CODE\_DEPLOY



&nbsp;   DATA\_PULL --> TRAIN --> EVAL --> REGISTRY --> BATCH\_DEPLOY



&nbsp;   EDGE\_COMMIT --> EDGE\_BUILD --> EDGE\_SIGN --> EDGE\_PUSH --> EDGE\_UPDATE




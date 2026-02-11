flowchart LR



&nbsp;   %% Edge Layer

&nbsp;   subgraph EDGE\["Local Edge Deployment"]

&nbsp;       EDGE\_APP\["Edge Gateway App<br/>Python Service"]

&nbsp;       EDGE\_BUF\["Local Buffer<br/>SQLite / Filesystem"]

&nbsp;       EDGE\_UPD\["Edge Auto‑Update Agent"]

&nbsp;   end



&nbsp;   %% Network

&nbsp;   NET\["Secure Network<br/>MQTT over TLS"]



&nbsp;   %% Cloud Ingestion Layer

&nbsp;   subgraph INGEST\["Cloud Ingestion Layer"]

&nbsp;       MQTT\_BROKER\["MQTT Broker"]

&nbsp;       STREAM\_PROC\["Stream Processor<br/>Validation • Enrichment"]

&nbsp;       DLQ\["Dead‑Letter Queue"]

&nbsp;   end



&nbsp;   %% Storage Layer

&nbsp;   subgraph STORAGE\["Cloud Storage Layer"]

&nbsp;       TSDB\["Time‑Series DB<br/>Curated 1‑min data"]

&nbsp;       OBJ\["Object Storage<br/>Raw + Processed"]

&nbsp;       META\["Metadata Store"]

&nbsp;   end



&nbsp;   %% ML Layer

&nbsp;   subgraph ML\["ML Training \& Batch Jobs"]

&nbsp;       TRAIN\_PIPE\["Training Pipeline<br/>CNN + LSTM"]

&nbsp;       MODEL\_REG\["Model Registry<br/>Versioned Models"]

&nbsp;       BATCH\_PRED\["Batch Prediction Jobs"]

&nbsp;   end



&nbsp;   %% Dashboard Layer

&nbsp;   subgraph DASH\["Dashboard Deployment"]

&nbsp;       TABLEAU\["Tableau Server / Cloud"]

&nbsp;       DASH\_UPD\["Scheduled Extract Refresh"]

&nbsp;   end



&nbsp;   %% CI/CD Layer

&nbsp;   subgraph CICD\["CI/CD Pipelines"]

&nbsp;       CODE\_PIPE\["Code Pipeline<br/>Build • Test • Deploy"]

&nbsp;       MODEL\_PIPE\["Model Pipeline<br/>Train • Validate • Register"]

&nbsp;       EDGE\_PIPE\["Edge Deployment Pipeline<br/>OTA Updates"]

&nbsp;   end



&nbsp;   %% Connections

&nbsp;   EDGE\_APP --> EDGE\_BUF --> NET --> MQTT\_BROKER --> STREAM\_PROC --> TSDB

&nbsp;   STREAM\_PROC --> OBJ

&nbsp;   STREAM\_PROC --> META

&nbsp;   STREAM\_PROC --> DLQ



&nbsp;   TSDB --> TRAIN\_PIPE --> MODEL\_REG --> BATCH\_PRED --> OBJ

&nbsp;   MODEL\_REG --> BATCH\_PRED



&nbsp;   OBJ --> TABLEAU

&nbsp;   TSDB --> TABLEAU

&nbsp;   TABLEAU --> DASH\_UPD



&nbsp;   CODE\_PIPE --> STREAM\_PROC

&nbsp;   CODE\_PIPE --> TABLEAU

&nbsp;   MODEL\_PIPE --> MODEL\_REG

&nbsp;   EDGE\_PIPE --> EDGE\_UPD




flowchart TB



&nbsp;   %% Ingestion Layer

&nbsp;   subgraph INGEST\["Cloud Ingestion Layer"]

&nbsp;       SP\["Stream Processor"]

&nbsp;       VAL\["Validation \& Enrichment"]

&nbsp;       ROUTE\["Routing Logic"]

&nbsp;   end



&nbsp;   %% Storage Layer

&nbsp;   subgraph STORAGE\["Cloud Storage Architecture"]

&nbsp;       TSDB\["Time‑Series Database<br/>• 1‑min curated data<br/>• Partitioned by house\_id"]

&nbsp;       OBJ\_RAW\["Object Storage: Raw Data<br/>• HDF5 files<br/>• Unprocessed streams"]

&nbsp;       OBJ\_PROC\["Object Storage: Processed Data<br/>• Cleaned CSVs<br/>• Resampled slices"]

&nbsp;       META\["Metadata Store<br/>• Appliance info<br/>• Meter mappings<br/>• Model versions"]

&nbsp;       ML\_OUT\["ML Output Store<br/>• NILM results<br/>• Forecast results"]

&nbsp;   end



&nbsp;   %% ML Layer

&nbsp;   subgraph ML\["Machine Learning Pipelines"]

&nbsp;       CNN\["CNN NILM Model"]

&nbsp;       LSTM\["LSTM/GRU Forecasting Model"]

&nbsp;   end



&nbsp;   %% Dashboard

&nbsp;   subgraph DASH\["Dashboard Layer"]

&nbsp;       TBL\["Tableau Dashboard"]

&nbsp;   end



&nbsp;   %% Ingestion to Storage

&nbsp;   SP --> VAL --> ROUTE

&nbsp;   ROUTE --> TSDB

&nbsp;   ROUTE --> OBJ\_RAW

&nbsp;   ROUTE --> OBJ\_PROC

&nbsp;   ROUTE --> META



&nbsp;   %% Storage to ML

&nbsp;   TSDB --> CNN

&nbsp;   TSDB --> LSTM

&nbsp;   OBJ\_PROC --> CNN

&nbsp;   OBJ\_PROC --> LSTM

&nbsp;   META --> CNN

&nbsp;   META --> LSTM



&nbsp;   %% ML Outputs

&nbsp;   CNN --> ML\_OUT

&nbsp;   LSTM --> ML\_OUT



&nbsp;   %% Dashboard

&nbsp;   ML\_OUT --> TBL

&nbsp;   TSDB --> TBL

&nbsp;   META --> TBL




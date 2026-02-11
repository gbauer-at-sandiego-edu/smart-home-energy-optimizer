flowchart TB



&nbsp;   %% Data Generation

&nbsp;   subgraph GEN\["1. Data Generation"]

&nbsp;       SM\["Smart Meter (Mains)"]

&nbsp;       AM\["Appliance Sub‑meters"]

&nbsp;   end



&nbsp;   %% Edge Processing

&nbsp;   subgraph EDGE\["2. Edge Processing"]

&nbsp;       CLEAN\_EDGE\["Light Cleaning<br/>Drop zeros, basic validation"]

&nbsp;       ALIGN\_EDGE\["Timestamp Alignment"]

&nbsp;       BUFFER\["Local Buffering<br/>(Outage Tolerance)"]

&nbsp;       SEND\["Publish via MQTT<br/>TLS + Auth"]

&nbsp;   end



&nbsp;   %% Cloud Ingestion

&nbsp;   subgraph INGEST\["3. Cloud Ingestion"]

&nbsp;       CONSUME\["Message Consumer"]

&nbsp;       VALIDATE\["Validation<br/>Schema, ranges, missing"]

&nbsp;       ENRICH\["Enrichment<br/>Metadata, timestamps"]

&nbsp;       NORMALIZE\["Normalization<br/>Units, field names"]

&nbsp;       ROUTE\["Routing<br/>TSDB • Raw • Processed • Metadata"]

&nbsp;   end



&nbsp;   %% Storage

&nbsp;   subgraph STORAGE\["4. Storage"]

&nbsp;       TSDB\["Time‑Series DB<br/>1‑min curated data"]

&nbsp;       RAW\["Object Storage (Raw)<br/>HDF5"]

&nbsp;       PROC\["Object Storage (Processed)<br/>Cleaned CSVs"]

&nbsp;       META\["Metadata Store"]

&nbsp;   end



&nbsp;   %% ML Pipelines

&nbsp;   subgraph ML\["5. Machine Learning"]

&nbsp;       CNN\["CNN NILM Model<br/>Appliance Disaggregation"]

&nbsp;       LSTM\["LSTM/GRU Model<br/>Next‑Hour Forecasting"]

&nbsp;       OUT\_CNN\["NILM Outputs"]

&nbsp;       OUT\_LSTM\["Forecast Outputs"]

&nbsp;   end



&nbsp;   %% Visualization

&nbsp;   subgraph DASH\["6. Visualization"]

&nbsp;       TBL\["Tableau Dashboard<br/>Status • Summary • ML Insights"]

&nbsp;   end



&nbsp;   %% Archival

&nbsp;   subgraph ARCHIVE\["7. Archival \& Long‑Term Storage"]

&nbsp;       ARCH\_RAW\["Raw Data Archive"]

&nbsp;       ARCH\_PROC\["Processed Data Archive"]

&nbsp;       ARCH\_ML\["ML Output Archive"]

&nbsp;   end



&nbsp;   %% Connections

&nbsp;   SM --> CLEAN\_EDGE

&nbsp;   AM --> CLEAN\_EDGE

&nbsp;   CLEAN\_EDGE --> ALIGN\_EDGE --> BUFFER --> SEND



&nbsp;   SEND --> CONSUME --> VALIDATE --> ENRICH --> NORMALIZE --> ROUTE



&nbsp;   ROUTE --> TSDB

&nbsp;   ROUTE --> RAW

&nbsp;   ROUTE --> PROC

&nbsp;   ROUTE --> META



&nbsp;   TSDB --> CNN --> OUT\_CNN --> TBL

&nbsp;   TSDB --> LSTM --> OUT\_LSTM --> TBL

&nbsp;   PROC --> CNN

&nbsp;   PROC --> LSTM



&nbsp;   RAW --> ARCH\_RAW

&nbsp;   PROC --> ARCH\_PROC

&nbsp;   OUT\_CNN --> ARCH\_ML

&nbsp;   OUT\_LSTM --> ARCH\_ML




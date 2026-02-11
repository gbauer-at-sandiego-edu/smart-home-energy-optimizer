flowchart LR



&nbsp;   %% Home Layer

&nbsp;   subgraph HOME\["Home Environment"]

&nbsp;       SM\["Smart Meter"]

&nbsp;       AM\["Appliance Sub‑meters"]

&nbsp;       EDGE\["Edge Gateway"]

&nbsp;   end



&nbsp;   %% Network Layer

&nbsp;   subgraph NET\["Network Layer"]

&nbsp;       MQTT\["MQTT Broker<br/>Secure Publish"]

&nbsp;   end



&nbsp;   %% Cloud Ingestion

&nbsp;   subgraph INGEST\["Cloud Ingestion"]

&nbsp;       PROC\["Stream Processing<br/>Validation • Enrichment • Routing"]

&nbsp;   end



&nbsp;   %% Storage Layer

&nbsp;   subgraph STORAGE\["Cloud Storage"]

&nbsp;       TSDB\["Time‑Series DB<br/>Curated 1‑min data"]

&nbsp;       OBJ\["Object Storage<br/>Raw + Processed"]

&nbsp;       META\["Metadata Store"]

&nbsp;   end



&nbsp;   %% ML Layer

&nbsp;   subgraph ML\["Machine Learning"]

&nbsp;       CNN\["CNN NILM Model"]

&nbsp;       LSTM\["LSTM Forecasting Model"]

&nbsp;   end



&nbsp;   %% Dashboard Layer

&nbsp;   subgraph DASH\["Dashboard"]

&nbsp;       TBL\["Tableau Visualizations<br/>Status • Summary • ML Insights"]

&nbsp;   end



&nbsp;   %% Connections

&nbsp;   SM --> EDGE

&nbsp;   AM --> EDGE

&nbsp;   EDGE --> MQTT --> PROC

&nbsp;   PROC --> TSDB

&nbsp;   PROC --> OBJ

&nbsp;   PROC --> META

&nbsp;   TSDB --> CNN --> TBL

&nbsp;   TSDB --> LSTM --> TBL

&nbsp;   OBJ --> CNN

&nbsp;   OBJ --> LSTM

&nbsp;   META --> TBL




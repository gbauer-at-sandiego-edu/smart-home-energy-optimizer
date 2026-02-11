flowchart LR



&nbsp;   %% MQTT Input

&nbsp;   MQTT\["MQTT Broker / IoT Hub<br/>TLS + Auth"]



&nbsp;   %% Stream Processor

&nbsp;   subgraph SP\["Stream Processing Layer"]

&nbsp;       CONSUME\["Message Consumer<br/>(MQTT → Stream)"]

&nbsp;       VALIDATE\["Validation<br/>• Schema check<br/>• Missing values<br/>• Range checks"]

&nbsp;       ENRICH\["Enrichment<br/>• Timestamps<br/>• House metadata<br/>• Appliance mapping"]

&nbsp;       NORMALIZE\["Normalization<br/>• Units<br/>• Field names<br/>• Types"]

&nbsp;       ROUTE\["Routing Logic<br/>• TSDB<br/>• Object Storage<br/>• Metadata"]

&nbsp;   end



&nbsp;   %% Storage Targets

&nbsp;   subgraph STORAGE\["Storage Targets"]

&nbsp;       TSDB\["Time‑Series DB<br/>1‑min curated data"]

&nbsp;       OBJ\_RAW\["Object Storage (Raw)<br/>HDF5 / raw streams"]

&nbsp;       OBJ\_PROC\["Object Storage (Processed)<br/>Cleaned CSVs"]

&nbsp;       META\["Metadata Store<br/>Appliances • Meters • Models"]

&nbsp;   end



&nbsp;   %% ML Pipelines

&nbsp;   subgraph ML\["Machine Learning Pipelines"]

&nbsp;       CNN\["CNN NILM Model"]

&nbsp;       LSTM\["LSTM/GRU Forecasting Model"]

&nbsp;   end



&nbsp;   %% Connections

&nbsp;   MQTT --> CONSUME --> VALIDATE --> ENRICH --> NORMALIZE --> ROUTE

&nbsp;   ROUTE --> TSDB

&nbsp;   ROUTE --> OBJ\_RAW

&nbsp;   ROUTE --> OBJ\_PROC

&nbsp;   ROUTE --> META



&nbsp;   TSDB --> CNN

&nbsp;   TSDB --> LSTM

&nbsp;   OBJ\_PROC --> CNN

&nbsp;   OBJ\_PROC --> LSTM




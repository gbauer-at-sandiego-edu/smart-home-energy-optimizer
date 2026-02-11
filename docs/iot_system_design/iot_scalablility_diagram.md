flowchart LR

&nbsp;   %% Multiple Homes

&nbsp;   subgraph H1\["Home 1"]

&nbsp;       SM1\["Smart Meter"]

&nbsp;       AM1\["Sub‑meters"]

&nbsp;       EDGE1\["Edge Gateway"]

&nbsp;   end



&nbsp;   subgraph H2\["Home 2"]

&nbsp;       SM2\["Smart Meter"]

&nbsp;       AM2\["Sub‑meters"]

&nbsp;       EDGE2\["Edge Gateway"]

&nbsp;   end



&nbsp;   subgraph H3\["Home N"]

&nbsp;       SM3\["Smart Meter"]

&nbsp;       AM3\["Sub‑meters"]

&nbsp;       EDGE3\["Edge Gateway"]

&nbsp;   end



&nbsp;   %% Network

&nbsp;   EDGE1 --> MQTT\["MQTT Broker Cluster"]

&nbsp;   EDGE2 --> MQTT

&nbsp;   EDGE3 --> MQTT



&nbsp;   %% Cloud Ingestion

&nbsp;   MQTT --> INGEST\["Horizontally Scalable<br/>Stream Processor Pool"]



&nbsp;   %% Partitioning

&nbsp;   INGEST -->|Partition by house\_id| TSDB\["Time‑Series DB<br/>Sharded Storage"]

&nbsp;   INGEST -->|Raw + Processed| DL\["Object Storage<br/>Unlimited Scale"]

&nbsp;   INGEST --> META\["Metadata Store"]



&nbsp;   %% ML Pipelines

&nbsp;   TSDB --> ML\_CNN\["CNN NILM<br/>Containerized / Serverless"]

&nbsp;   TSDB --> ML\_LSTM\["LSTM/GRU Forecasting<br/>Containerized / Serverless"]



&nbsp;   %% Outputs

&nbsp;   ML\_CNN --> DASH\["Multi‑Tenant Dashboard"]

&nbsp;   ML\_LSTM --> DASH




flowchart LR



&nbsp;   %% External Actors

&nbsp;   subgraph ACTORS\["External Actors (Outside System Boundary)"]

&nbsp;       USER\["End User / Homeowner"]

&nbsp;       ADMIN\["System Administrator"]

&nbsp;       UTIL\["Utility Provider (Optional)"]

&nbsp;       CLOUD\_SERV\["Cloud Provider Services"]

&nbsp;   end



&nbsp;   %% System Boundary

&nbsp;   subgraph SYSTEM\["Smart Energy Monitoring System (System Boundary)"]

&nbsp;       

&nbsp;       subgraph EDGE\["Edge Layer"]

&nbsp;           SM\["Smart Meter / Sub‑meters"]

&nbsp;           GATEWAY\["Edge Gateway<br/>Buffering + MQTT Client"]

&nbsp;       end



&nbsp;       subgraph CLOUD\["Cloud Layer"]

&nbsp;           MQTT\["MQTT Broker"]

&nbsp;           INGEST\["Ingestion Service<br/>Validation • Enrichment"]

&nbsp;           TSDB\["Time‑Series DB"]

&nbsp;           OBJ\["Object Storage"]

&nbsp;           META\["Metadata Store"]

&nbsp;       end



&nbsp;       subgraph ML\["ML Layer"]

&nbsp;           CNN\["CNN NILM Model"]

&nbsp;           LSTM\["LSTM Forecast Model"]

&nbsp;           BATCH\["Batch Prediction Jobs"]

&nbsp;       end



&nbsp;       subgraph DASH\["Dashboard Layer"]

&nbsp;           TABLEAU\["Dashboard (Tableau)"]

&nbsp;       end



&nbsp;   end



&nbsp;   %% Interfaces

&nbsp;   USER --> TABLEAU

&nbsp;   ADMIN --> META

&nbsp;   ADMIN --> INGEST

&nbsp;   UTIL --> TSDB



&nbsp;   GATEWAY --> MQTT

&nbsp;   MQTT --> INGEST

&nbsp;   INGEST --> TSDB

&nbsp;   INGEST --> OBJ

&nbsp;   INGEST --> META



&nbsp;   TSDB --> CNN

&nbsp;   TSDB --> LSTM

&nbsp;   OBJ --> CNN

&nbsp;   OBJ --> LSTM



&nbsp;   CNN --> BATCH

&nbsp;   LSTM --> BATCH

&nbsp;   BATCH --> OBJ



&nbsp;   OBJ --> TABLEAU

&nbsp;   TSDB --> TABLEAU

&nbsp;   META --> TABLEAU



&nbsp;   CLOUD\_SERV --> SYSTEM




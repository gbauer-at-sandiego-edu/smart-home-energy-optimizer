flowchart TB



&nbsp;   %% Home Layer

&nbsp;   subgraph HOME\["🏠 Home Environment"]

&nbsp;       SM\["Smart Meter (Mains)"]

&nbsp;       AM\["Appliance Sub‑meters"]

&nbsp;       EDGE\["Edge Gateway Device<br/>(Raspberry Pi‑class)"]

&nbsp;   end



&nbsp;   %% Network Layer

&nbsp;   subgraph NETWORK\["🌐 Network Layer"]

&nbsp;       WIFI\["Home Wi‑Fi / Ethernet"]

&nbsp;       MQTT\["MQTT Broker (Cloud or Managed IoT Hub)"]

&nbsp;   end



&nbsp;   %% Cloud Ingestion Layer

&nbsp;   subgraph INGEST\["☁️ Cloud Ingestion Layer"]

&nbsp;       SP\["Stream Processor Pool<br/>(Kafka Consumer / Serverless Functions)"]

&nbsp;       VAL\["Validation \& Enrichment"]

&nbsp;       ROUTE\["Routing to Storage \& ML Pipelines"]

&nbsp;   end



&nbsp;   %% Storage Layer

&nbsp;   subgraph STORAGE\["🗄️ Cloud Storage Layer"]

&nbsp;       TSDB\["Time‑Series Database<br/>(Sharded, 1‑min data)"]

&nbsp;       OBJ\["Object Storage<br/>(Raw + Processed Files)"]

&nbsp;       META\["Metadata Store<br/>(Appliances, Meters, Models)"]

&nbsp;   end



&nbsp;   %% ML Layer

&nbsp;   subgraph ML\["🤖 Machine Learning Layer"]

&nbsp;       CNN\["CNN NILM Model<br/>(Containerized / Serverless)"]

&nbsp;       LSTM\["LSTM/GRU Forecasting Model<br/>(Containerized / Serverless)"]

&nbsp;   end



&nbsp;   %% Dashboard Layer

&nbsp;   subgraph DASH\["📊 Dashboard Layer"]

&nbsp;       TBL\["Tableau Dashboard<br/>Status • Summary • ML Insights"]

&nbsp;   end



&nbsp;   %% Connections

&nbsp;   SM --> EDGE

&nbsp;   AM --> EDGE

&nbsp;   EDGE --> WIFI --> MQTT

&nbsp;   MQTT --> SP --> VAL --> ROUTE

&nbsp;   ROUTE --> TSDB

&nbsp;   ROUTE --> OBJ

&nbsp;   ROUTE --> META

&nbsp;   TSDB --> CNN

&nbsp;   TSDB --> LSTM

&nbsp;   OBJ --> CNN

&nbsp;   OBJ --> LSTM

&nbsp;   CNN --> TBL

&nbsp;   LSTM --> TBL




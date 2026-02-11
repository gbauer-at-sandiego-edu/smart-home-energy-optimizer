flowchart TB



&nbsp;   %% Home Layer

&nbsp;   subgraph HOME\["🏠 Home Environment"]

&nbsp;       SM\["Smart Meter (Mains)"]

&nbsp;       AM\["Appliance Sub‑meters"]

&nbsp;       EDGE\["Edge Gateway<br/>(Raspberry Pi‑class)"]

&nbsp;   end



&nbsp;   %% Network Layer

&nbsp;   subgraph NET\["🌐 Network Layer"]

&nbsp;       WIFI\["Home Wi‑Fi / Ethernet"]

&nbsp;       MQTT\["MQTT Broker / IoT Hub<br/>(TLS + Auth)"]

&nbsp;   end



&nbsp;   %% Cloud Ingestion

&nbsp;   subgraph INGEST\["☁️ Cloud Ingestion Layer"]

&nbsp;       SP\["Stream Processor Pool<br/>(Kafka / Serverless)"]

&nbsp;       VAL\["Validation \& Enrichment"]

&nbsp;       ROUTE\["Routing to Storage \& ML Pipelines"]

&nbsp;   end



&nbsp;   %% Storage Layer

&nbsp;   subgraph STORAGE\["🗄️ Cloud Storage Layer"]

&nbsp;       TSDB\["Time‑Series DB<br/>Sharded 1‑min data"]

&nbsp;       OBJ\["Object Storage<br/>Raw + Processed Files"]

&nbsp;       META\["Metadata Store<br/>Appliances • Meters • Models"]

&nbsp;   end



&nbsp;   %% ML Layer

&nbsp;   subgraph ML\["🤖 Machine Learning Layer"]

&nbsp;       CNN\["CNN NILM Model<br/>Appliance Disaggregation"]

&nbsp;       LSTM\["LSTM/GRU Model<br/>Next‑Hour Forecasting"]

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




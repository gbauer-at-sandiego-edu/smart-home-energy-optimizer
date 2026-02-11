flowchart TB



&nbsp;   %% Home Layer

&nbsp;   subgraph Home\["Home Environment"]

&nbsp;       SM\["Smart Meter (Mains)"]

&nbsp;       AM\["Appliance Sub-meters"]

&nbsp;       EDGE\["Edge Gateway Device"]

&nbsp;   end



&nbsp;   %% Network Layer

&nbsp;   subgraph Network\["Network Layer"]

&nbsp;       WIFI\["Wi-Fi / Ethernet"]

&nbsp;       MQTT\["MQTT Broker / IoT Hub"]

&nbsp;   end



&nbsp;   %% Cloud Ingestion

&nbsp;   subgraph Ingestion\["Cloud Ingestion"]

&nbsp;       SP\["Stream Processor"]

&nbsp;       VAL\["Validation and Enrichment"]

&nbsp;       ROUTE\["Routing to Storage and ML"]

&nbsp;   end



&nbsp;   %% Storage Layer

&nbsp;   subgraph Storage\["Storage Layer"]

&nbsp;       TSDB\["Time-Series Database"]

&nbsp;       OBJ\["Object Storage"]

&nbsp;       META\["Metadata Store"]

&nbsp;   end



&nbsp;   %% ML Layer

&nbsp;   subgraph ML\["Machine Learning"]

&nbsp;       CNN\["CNN NILM Model"]

&nbsp;       LSTM\["LSTM/GRU Forecasting Model"]

&nbsp;   end



&nbsp;   %% Dashboard Layer

&nbsp;   subgraph Dashboard\["Dashboard"]

&nbsp;       TBL\["Tableau Dashboard"]

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




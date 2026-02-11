sequenceDiagram

&nbsp;   autonumber



&nbsp;   participant SM as Smart Meter (Mains)

&nbsp;   participant AM as Appliance Sub‑meters

&nbsp;   participant EDGE as Edge Gateway

&nbsp;   participant MQTT as MQTT Broker / IoT Hub

&nbsp;   participant INGEST as Cloud Ingestion<br/>(Stream Processor)

&nbsp;   participant TSDB as Time‑Series DB

&nbsp;   participant DL as Object Storage

&nbsp;   participant ML as ML Pipelines<br/>(CNN NILM + LSTM Forecasting)

&nbsp;   participant DASH as Tableau Dashboard



&nbsp;   %% Sensor Emission

&nbsp;   SM->>EDGE: Emit mains power reading<br/>(1–6 sec)

&nbsp;   AM->>EDGE: Emit appliance-level readings



&nbsp;   %% Edge Processing

&nbsp;   EDGE->>EDGE: Timestamp normalization<br/>Light cleaning

&nbsp;   EDGE->>EDGE: Optional 1‑min downsampling

&nbsp;   EDGE->>MQTT: Publish readings via MQTT<br/>TLS + Auth



&nbsp;   %% Cloud Ingestion

&nbsp;   MQTT->>INGEST: Deliver messages<br/>QoS handling

&nbsp;   INGEST->>INGEST: Validate + enrich data

&nbsp;   INGEST->>TSDB: Write curated 1‑min data

&nbsp;   INGEST->>DL: Store raw + processed files

&nbsp;   INGEST->>TSDB: Update metadata entries



&nbsp;   %% ML Pipelines

&nbsp;   TSDB->>ML: Provide curated time‑series windows

&nbsp;   DL->>ML: Provide raw data for training

&nbsp;   ML->>TSDB: Store NILM + forecast outputs



&nbsp;   %% Dashboard

&nbsp;   TSDB->>DASH: Current status metrics

&nbsp;   TSDB->>DASH: Historical summaries

&nbsp;   ML->>DASH: NILM appliance breakdown

&nbsp;   ML->>DASH: Next‑hour forecast results




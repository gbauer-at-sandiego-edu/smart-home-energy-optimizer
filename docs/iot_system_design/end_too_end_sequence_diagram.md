sequenceDiagram

&nbsp;   autonumber



&nbsp;   participant SM as Smart Meter

&nbsp;   participant EDGE as Edge Gateway

&nbsp;   participant MQTT as MQTT Broker

&nbsp;   participant INGEST as Cloud Ingestion

&nbsp;   participant TSDB as Time‑Series DB

&nbsp;   participant OBJ as Object Storage

&nbsp;   participant ML as ML Models (CNN + LSTM)

&nbsp;   participant DASH as Dashboard (Tableau)



&nbsp;   SM->>EDGE: Send mains/appliance readings

&nbsp;   EDGE->>EDGE: Local buffering + retry logic

&nbsp;   EDGE->>MQTT: Publish message (TLS + Auth)



&nbsp;   MQTT->>INGEST: Forward message

&nbsp;   INGEST->>INGEST: Schema validation

&nbsp;   INGEST->>INGEST: Metadata enrichment

&nbsp;   INGEST->>TSDB: Write curated 1‑min data

&nbsp;   INGEST->>OBJ: Store raw/processed files



&nbsp;   ML->>TSDB: Read curated data

&nbsp;   ML->>OBJ: Read raw/processed data

&nbsp;   ML->>ML: Run CNN NILM + LSTM Forecasting

&nbsp;   ML->>OBJ: Save model outputs (CSV)

&nbsp;   ML->>TSDB: Write derived metrics (optional)



&nbsp;   DASH->>TSDB: Query curated data

&nbsp;   DASH->>OBJ: Query ML outputs

&nbsp;   DASH->>DASH: Render views (Status, NILM, Forecast)




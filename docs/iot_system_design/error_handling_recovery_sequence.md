sequenceDiagram

&nbsp;   autonumber



&nbsp;   participant SM as Smart Meter

&nbsp;   participant EDGE as Edge Gateway

&nbsp;   participant MQTT as MQTT Broker

&nbsp;   participant INGEST as Cloud Ingestion

&nbsp;   participant DLQ as Dead‑Letter Queue

&nbsp;   participant TSDB as Time‑Series DB

&nbsp;   participant ML as ML Models

&nbsp;   participant DASH as Dashboard



&nbsp;   %% Edge Failure + Recovery

&nbsp;   SM->>EDGE: Send reading

&nbsp;   EDGE->>EDGE: Write to local buffer

&nbsp;   EDGE->>MQTT: Publish message

&nbsp;   MQTT--xEDGE: Network failure

&nbsp;   EDGE->>EDGE: Retry with backoff

&nbsp;   EDGE->>MQTT: Reconnect + republish



&nbsp;   %% Ingestion Failure + DLQ

&nbsp;   MQTT->>INGEST: Deliver message

&nbsp;   INGEST--xINGEST: Schema validation fails

&nbsp;   INGEST->>DLQ: Route message to DLQ

&nbsp;   INGEST->>INGEST: Log error + alert



&nbsp;   %% Successful Ingestion After Recovery

&nbsp;   EDGE->>MQTT: Republish corrected message

&nbsp;   MQTT->>INGEST: Deliver message

&nbsp;   INGEST->>TSDB: Write curated data



&nbsp;   %% ML Pipeline Error + Fallback

&nbsp;   ML->>TSDB: Read data

&nbsp;   ML--xML: Model load failure

&nbsp;   ML->>ML: Load fallback model

&nbsp;   ML->>TSDB: Write predictions



&nbsp;   %% Dashboard Degradation + Recovery

&nbsp;   DASH->>TSDB: Query data

&nbsp;   TSDB--xDASH: Query timeout

&nbsp;   DASH->>DASH: Use cached view

&nbsp;   DASH->>TSDB: Retry query

&nbsp;   TSDB->>DASH: Return fresh data




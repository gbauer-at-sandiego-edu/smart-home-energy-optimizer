flowchart TB



&nbsp;   %% Edge Reliability

&nbsp;   subgraph EDGE\["Edge Reliability"]

&nbsp;       BUF\["Local Buffering<br/>Stores data during outages"]

&nbsp;       RETRY\_EDGE\["Retry Logic<br/>Exponential backoff"]

&nbsp;       HEALTH\_EDGE\["Health Checks<br/>Device heartbeat"]

&nbsp;   end



&nbsp;   %% Network Reliability

&nbsp;   subgraph NET\["Network Reliability"]

&nbsp;       TLS\["TLS Encryption<br/>Protects against corruption"]

&nbsp;       QOS\["MQTT QoS Levels<br/>At least once / exactly once"]

&nbsp;       RECONNECT\["Auto‑Reconnect<br/>Network recovery"]

&nbsp;   end



&nbsp;   %% Cloud Ingestion Reliability

&nbsp;   subgraph INGEST\["Cloud Ingestion Reliability"]

&nbsp;       RETRY\_INGEST\["Retry on Failure<br/>Backoff + jitter"]

&nbsp;       DLQ\["Dead‑Letter Queue<br/>Stores failed messages"]

&nbsp;       SCALE\["Auto‑Scaling<br/>Handles load spikes"]

&nbsp;   end



&nbsp;   %% Storage Durability

&nbsp;   subgraph STORAGE\["Storage Durability"]

&nbsp;       REPL\["Replication<br/>Multi‑AZ copies"]

&nbsp;       VERSION\["Versioning<br/>Protects against overwrite"]

&nbsp;       CHECKSUM\["Checksums<br/>Detect corruption"]

&nbsp;   end



&nbsp;   %% ML Pipeline Reliability

&nbsp;   subgraph ML\["ML Pipeline Reliability"]

&nbsp;       FALLBACK\["Fallback Models<br/>Use last known good model"]

&nbsp;       CHECKPOINT\["Model Checkpoints<br/>Periodic saves"]

&nbsp;       VALIDATE\_ML\["Input Validation<br/>Reject bad sequences"]

&nbsp;   end



&nbsp;   %% Dashboard Continuity

&nbsp;   subgraph DASH\["Dashboard Continuity"]

&nbsp;       CACHE\["Cached Views<br/>Last known data"]

&nbsp;       RETRY\_DASH\["Retry Queries<br/>Graceful degradation"]

&nbsp;       ALERTS\["Alerts \& Notifications<br/>System health"]

&nbsp;   end



&nbsp;   %% Connections

&nbsp;   BUF --> RETRY\_EDGE --> HEALTH\_EDGE --> TLS --> QOS --> RECONNECT --> RETRY\_INGEST --> DLQ --> SCALE --> REPL --> VERSION --> CHECKSUM --> FALLBACK --> CHECKPOINT --> VALIDATE\_ML --> CACHE --> RETRY\_DASH --> ALERTS




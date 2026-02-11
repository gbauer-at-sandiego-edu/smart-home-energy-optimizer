flowchart LR



&nbsp;   %% Edge Processing

&nbsp;   subgraph EDGE\["Edge Gateway Processing"]

&nbsp;       EP1\["Timestamp Normalization"]

&nbsp;       EP2\["Light Cleaning<br/>(drop zeros, basic validation)"]

&nbsp;       EP3\["Optional 1‑min Downsampling"]

&nbsp;       EP4\["Local Buffering<br/>(Outage Tolerance)"]

&nbsp;       EP5\["Low‑latency Alerts<br/>(e.g., overload detection)"]

&nbsp;   end



&nbsp;   %% Cloud Processing

&nbsp;   subgraph CLOUD\["Cloud Processing"]

&nbsp;       CP1\["Stream Ingestion<br/>(MQTT → Processor)"]

&nbsp;       CP2\["Deep Cleaning \& Enrichment"]

&nbsp;       CP3\["Long‑term Storage<br/>(TSDB + Object Storage)"]

&nbsp;       CP4\["CNN NILM Inference"]

&nbsp;       CP5\["LSTM/GRU Forecasting"]

&nbsp;       CP6\["Historical Analytics<br/>(Daily/Weekly Trends)"]

&nbsp;       CP7\["Dashboard Rendering"]

&nbsp;   end



&nbsp;   %% Tradeoff Arrows

&nbsp;   EDGE -->|Low latency<br/>Bandwidth reduction| CLOUD

&nbsp;   CLOUD -->|Model updates<br/>Configuration| EDGE




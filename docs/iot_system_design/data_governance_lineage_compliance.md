flowchart TB



&nbsp;   %% Data Lineage

&nbsp;   subgraph LINEAGE\["Data Lineage Tracking"]

&nbsp;       RAW\_SRC\["Raw Source<br/>Smart Meter / Sub‑meters"]

&nbsp;       PROC\_STEP\["Processing Steps<br/>Validation • Cleaning • Resampling"]

&nbsp;       FEAT\_STEP\["Feature Engineering<br/>CNN + LSTM"]

&nbsp;       MODEL\_STEP\["Model Outputs<br/>NILM + Forecasting"]

&nbsp;       DASH\_STEP\["Dashboard Consumption"]

&nbsp;   end



&nbsp;   %% Data Quality

&nbsp;   subgraph QUALITY\["Data Quality Controls"]

&nbsp;       SCHEMA\["Schema Validation"]

&nbsp;       RANGE\["Range Checks"]

&nbsp;       DUP\["Duplicate Detection"]

&nbsp;       MISSING\["Missing Value Flags"]

&nbsp;       QUALITY\_SCORE\["Quality Score per Record"]

&nbsp;   end



&nbsp;   %% Retention \& Lifecycle

&nbsp;   subgraph RETAIN\["Retention \& Lifecycle Policies"]

&nbsp;       RAW\_RET\["Raw Data Retention<br/>90 days"]

&nbsp;       CURATED\_RET\["Curated Data Retention<br/>1 year"]

&nbsp;       ML\_RET\["ML Outputs Retention<br/>6 months"]

&nbsp;       ARCHIVE\["Cold Storage Archive<br/>Long‑term retention"]

&nbsp;   end



&nbsp;   %% Access Control

&nbsp;   subgraph ACCESS\["Access Control \& Permissions"]

&nbsp;       ROLE\_INGEST\["Ingestion Role<br/>Write‑only"]

&nbsp;       ROLE\_ML\["ML Role<br/>Read curated • Write outputs"]

&nbsp;       ROLE\_DASH\["Dashboard Role<br/>Read‑only"]

&nbsp;       ROLE\_ADMIN\["Admin Role<br/>Full access + audit"]

&nbsp;   end



&nbsp;   %% Audit \& Compliance

&nbsp;   subgraph AUDIT\["Audit \& Compliance"]

&nbsp;       AUDIT\_LOGS\["Audit Logs<br/>Access + Changes"]

&nbsp;       VERSIONING\["Versioning<br/>Files + Models"]

&nbsp;       TRACE\["End‑to‑End Traceability<br/>Record → Dashboard"]

&nbsp;   end



&nbsp;   %% Connections

&nbsp;   RAW\_SRC --> PROC\_STEP --> FEAT\_STEP --> MODEL\_STEP --> DASH\_STEP



&nbsp;   PROC\_STEP --> SCHEMA

&nbsp;   PROC\_STEP --> RANGE

&nbsp;   PROC\_STEP --> DUP

&nbsp;   PROC\_STEP --> MISSING

&nbsp;   QUALITY\_SCORE --> DASH\_STEP



&nbsp;   RAW\_SRC --> RAW\_RET

&nbsp;   PROC\_STEP --> CURATED\_RET

&nbsp;   MODEL\_STEP --> ML\_RET

&nbsp;   CURATED\_RET --> ARCHIVE



&nbsp;   ROLE\_INGEST --> RAW\_SRC

&nbsp;   ROLE\_ML --> FEAT\_STEP

&nbsp;   ROLE\_DASH --> DASH\_STEP

&nbsp;   ROLE\_ADMIN --> AUDIT\_LOGS



&nbsp;   AUDIT\_LOGS --> TRACE

&nbsp;   VERSIONING --> TRACE




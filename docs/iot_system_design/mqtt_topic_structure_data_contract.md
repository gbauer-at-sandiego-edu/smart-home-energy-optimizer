flowchart TB



&nbsp;   %% Topic Hierarchy

&nbsp;   subgraph TOPICS\["MQTT Topic Hierarchy"]

&nbsp;       ROOT\["iot/"]

&nbsp;       HOUSE\["iot/{house\_id}/"]

&nbsp;       MAINS\["iot/{house\_id}/mains"]

&nbsp;       APPLIANCE\["iot/{house\_id}/appliance/{appliance\_id}"]

&nbsp;       STATUS\["iot/{house\_id}/status"]

&nbsp;   end



&nbsp;   %% Data Contract (JSON replaced with safe field list)

&nbsp;   subgraph CONTRACT\["Data Contract Fields"]

&nbsp;       PAYLOAD\["Fields:

\- house\_id

\- appliance\_id

\- timestamp

\- power

\- voltage

\- current

\- frequency"]

&nbsp;   end



&nbsp;   %% Ingestion Routing

&nbsp;   subgraph ROUTE\["Ingestion Routing Logic"]

&nbsp;       VALIDATE\["Schema Validation"]

&nbsp;       ENRICH\["Metadata Enrichment"]

&nbsp;       NORMALIZE\["Normalization"]

&nbsp;       STORE\_TSDB\["Write to TSDB"]

&nbsp;       STORE\_RAW\["Write Raw to Object Storage"]

&nbsp;       STORE\_META\["Update Metadata Store"]

&nbsp;   end



&nbsp;   %% Connections

&nbsp;   ROOT --> HOUSE --> MAINS --> PAYLOAD

&nbsp;   HOUSE --> APPLIANCE --> PAYLOAD

&nbsp;   HOUSE --> STATUS



&nbsp;   PAYLOAD --> VALIDATE --> ENRICH --> NORMALIZE

&nbsp;   NORMALIZE --> STORE\_TSDB

&nbsp;   NORMALIZE --> STORE\_RAW

&nbsp;   ENRICH --> STORE\_META




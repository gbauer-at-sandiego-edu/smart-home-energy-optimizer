flowchart TB



&nbsp;   %% TSDB Schema

&nbsp;   subgraph TSDB\["Time‑Series Database (Curated 1‑min Data)"]

&nbsp;       TSDB\_FIELDS\["Fields:

\- timestamp

\- house\_id

\- mains\_power

\- voltage

\- current

\- frequency

\- appliance\_power (optional)

\- quality\_flag"]

&nbsp;       TSDB\_KEYS\["Primary Keys:

\- timestamp

\- house\_id"]

&nbsp;       TSDB\_PART\["Partitioning:

\- By house\_id

\- By day/month"]

&nbsp;   end



&nbsp;   %% Object Storage Schema

&nbsp;   subgraph OBJ\["Object Storage (Raw + Processed)"]

&nbsp;       RAW\["Raw HDF5 Files:

\- ukdale\_house\_1.h5

\- ukdale\_house\_2.h5

\- full-resolution streams"]

&nbsp;       PROC\["Processed CSVs:

\- house\_1\_cleaned.csv

\- house\_2\_cleaned.csv

\- 1‑min aligned data"]

&nbsp;       OBJ\_META\["Object Metadata:

\- file\_size

\- checksum

\- ingestion\_timestamp"]

&nbsp;   end



&nbsp;   %% Metadata Store Schema

&nbsp;   subgraph META\["Metadata Store"]

&nbsp;       APPL\["Appliance Table:

\- appliance\_id

\- house\_id

\- appliance\_name

\- type

\- rated\_power"]

&nbsp;       METER\["Meter Table:

\- meter\_id

\- house\_id

\- location

\- sampling\_rate"]

&nbsp;       MODEL\["Model Versions:

\- model\_name

\- version

\- training\_date

\- metrics"]

&nbsp;   end



&nbsp;   %% Connections

&nbsp;   TSDB --> META

&nbsp;   OBJ --> META

&nbsp;   META --> TSDB




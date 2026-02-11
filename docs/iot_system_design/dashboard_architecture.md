flowchart LR



&nbsp;   %% Data Sources

&nbsp;   subgraph SOURCES\["Data Sources"]

&nbsp;       TSDB\["Time‑Series DB<br/>Curated 1‑min data"]

&nbsp;       OBJ\["Object Storage<br/>ML Outputs (CSV)"]

&nbsp;       META\["Metadata Store<br/>Appliances • Houses • Models"]

&nbsp;   end



&nbsp;   %% Tableau Server

&nbsp;   subgraph TABLEAU\["Tableau Server / Cloud"]

&nbsp;       EXTRACTS\["Data Extracts<br/>Scheduled Refresh"]

&nbsp;       LIVE\_CONN\["Live Connections<br/>TSDB Queries"]

&nbsp;       CACHE\["Cached Views<br/>Fallback during outages"]

&nbsp;   end



&nbsp;   %% Dashboard Views

&nbsp;   subgraph VIEWS\["Dashboard Views"]

&nbsp;       STATUS\["System Status View<br/>Live usage + health"]

&nbsp;       NILM\_VIEW\["NILM View<br/>Appliance‑level breakdown"]

&nbsp;       FORECAST\_VIEW\["Forecast View<br/>Next‑hour predictions"]

&nbsp;       ENERGY\_SUM\["Energy Summary<br/>Daily/weekly/monthly"]

&nbsp;   end



&nbsp;   %% Connections

&nbsp;   TSDB --> LIVE\_CONN --> STATUS

&nbsp;   TSDB --> EXTRACTS --> ENERGY\_SUM



&nbsp;   OBJ --> EXTRACTS --> NILM\_VIEW

&nbsp;   OBJ --> EXTRACTS --> FORECAST\_VIEW



&nbsp;   META --> EXTRACTS

&nbsp;   META --> LIVE\_CONN



&nbsp;   TABLEAU --> CACHE

&nbsp;   CACHE --> STATUS

&nbsp;   CACHE --> NILM\_VIEW

&nbsp;   CACHE --> FORECAST\_VIEW

&nbsp;   CACHE --> ENERGY\_SUM




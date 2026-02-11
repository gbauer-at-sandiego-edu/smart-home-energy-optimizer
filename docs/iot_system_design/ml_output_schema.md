flowchart TB



&nbsp;   %% NILM Output Schema

&nbsp;   subgraph NILM\["NILM Output Schema (CNN)"]

&nbsp;       NILM\_FIELDS\["Fields:

\- timestamp

\- house\_id

\- appliance\_id

\- appliance\_name

\- predicted\_state (0/1)

\- confidence\_score

\- power\_estimate (optional)"]

&nbsp;       NILM\_KEYS\["Primary Keys:

\- timestamp

\- house\_id

\- appliance\_id"]

&nbsp;   end



&nbsp;   %% Forecast Output Schema

&nbsp;   subgraph FORECAST\["Forecast Output Schema (LSTM)"]

&nbsp;       FORECAST\_FIELDS\["Fields:

\- timestamp

\- house\_id

\- predicted\_usage\_next\_hour

\- lower\_bound

\- upper\_bound

\- model\_version"]

&nbsp;       FORECAST\_KEYS\["Primary Keys:

\- timestamp

\- house\_id"]

&nbsp;   end



&nbsp;   %% Storage

&nbsp;   subgraph STORAGE\["ML Output Storage"]

&nbsp;       ML\_OUT\["ML Output Store:

\- nilm\_results.csv

\- forecast\_results.csv

\- versioned model outputs"]

&nbsp;   end



&nbsp;   %% Dashboard

&nbsp;   subgraph DASH\["Dashboard Consumption"]

&nbsp;       NILM\_VIEW\["NILM View<br/>Appliance breakdown"]

&nbsp;       FORECAST\_VIEW\["Forecast View<br/>Predicted vs actual"]

&nbsp;   end



&nbsp;   %% Connections

&nbsp;   NILM\_FIELDS --> ML\_OUT

&nbsp;   FORECAST\_FIELDS --> ML\_OUT



&nbsp;   ML\_OUT --> NILM\_VIEW

&nbsp;   ML\_OUT --> FORECAST\_VIEW




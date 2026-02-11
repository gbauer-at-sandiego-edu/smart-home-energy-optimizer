flowchart TB



&nbsp;   %% Data Sources

&nbsp;   subgraph SOURCES\["Data Sources"]

&nbsp;       TSDB\["Time‑Series DB<br/>1‑min curated data"]

&nbsp;       ML\_OUT\["ML Outputs<br/>NILM + Forecasts"]

&nbsp;       META\["Metadata Store<br/>Appliances • Meters • Models"]

&nbsp;   end



&nbsp;   %% Data Prep Layer

&nbsp;   subgraph PREP\["Dashboard Data Preparation"]

&nbsp;       EXTRACT\["Extract Data<br/>TSDB + ML + Metadata"]

&nbsp;       JOIN\["Join \& Merge<br/>Align timestamps, house\_id"]

&nbsp;       CALC\["Calculated Fields<br/>Daily totals, % breakdowns"]

&nbsp;       AGG\["Aggregation<br/>Hourly • Daily • Weekly"]

&nbsp;   end



&nbsp;   %% Dashboard Layer

&nbsp;   subgraph DASH\["Dashboard Layer (Tableau)"]

&nbsp;       STATUS\["Status View<br/>Current usage, alerts"]

&nbsp;       SUMMARY\["Summary View<br/>Daily/weekly totals"]

&nbsp;       NILM\_VIEW\["NILM View<br/>Appliance breakdown"]

&nbsp;       FORECAST\_VIEW\["Forecast View<br/>Predicted vs actual"]

&nbsp;       EXPORT\["Export Options<br/>CSV • PNG • PDF"]

&nbsp;   end



&nbsp;   %% Connections

&nbsp;   TSDB --> EXTRACT

&nbsp;   ML\_OUT --> EXTRACT

&nbsp;   META --> EXTRACT



&nbsp;   EXTRACT --> JOIN --> CALC --> AGG



&nbsp;   AGG --> STATUS

&nbsp;   AGG --> SUMMARY

&nbsp;   AGG --> NILM\_VIEW

&nbsp;   AGG --> FORECAST\_VIEW



&nbsp;   NILM\_VIEW --> EXPORT

&nbsp;   FORECAST\_VIEW --> EXPORT

&nbsp;   SUMMARY --> EXPORT




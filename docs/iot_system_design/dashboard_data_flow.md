flowchart LR

&nbsp;   %% Data Sources

&nbsp;   TSDB\["Time‑Series DB<br/>1‑Minute Curated Data"]

&nbsp;   META\["Metadata Store<br/>Appliances • Meters • House Info"]

&nbsp;   OUT\_CNN\["NILM Outputs<br/>Appliance ON/OFF"]

&nbsp;   OUT\_LSTM\["Forecast Outputs<br/>Next‑Hour Usage"]



&nbsp;   %% Preprocessing for Dashboard

&nbsp;   PREP\_STATUS\["Status Metrics<br/>Current Usage / Forecast"]

&nbsp;   PREP\_SUMMARY\["Summary Metrics<br/>Daily • Weekly Trends"]

&nbsp;   PREP\_NILM\["NILM Breakdown<br/>Appliance-Level Energy"]

&nbsp;   PREP\_FORECAST\["Forecast Comparison<br/>Predicted vs Actual"]



&nbsp;   %% Dashboard

&nbsp;   DASH\["Tableau Dashboard<br/>Status • Summary • ML Insights"]



&nbsp;   %% Connections

&nbsp;   TSDB --> PREP\_STATUS --> DASH

&nbsp;   TSDB --> PREP\_SUMMARY --> DASH

&nbsp;   OUT\_CNN --> PREP\_NILM --> DASH

&nbsp;   OUT\_LSTM --> PREP\_FORECAST --> DASH

&nbsp;   META --> DASH




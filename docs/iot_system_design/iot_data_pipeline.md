flowchart LR

&nbsp;   %% Raw Data

&nbsp;   RAW\["Raw UK‑DALE Data<br/>(HDF5: ukdale.h5)"]



&nbsp;   %% Ingestion

&nbsp;   INGEST\["Ingestion Script<br/>data\_ingest.py"]

&nbsp;   CLEAN\["Cleaning \& Validation<br/>Interpolation, clipping"]

&nbsp;   RESAMPLE\["Resampling<br/>1‑minute interval"]

&nbsp;   SLICE\["180‑Day Slice<br/>Aligned across houses"]



&nbsp;   %% Processed Data

&nbsp;   PROC\["Processed CSVs<br/>House\_1\_cleaned.csv<br/>House\_2\_cleaned.csv"]



&nbsp;   %% Modeling

&nbsp;   WIN\_CNN\["Windowing for CNN<br/>(Sliding windows)"]

&nbsp;   WIN\_LSTM\["Windowing for LSTM<br/>(Past 24h → Next hour)"]



&nbsp;   CNN\["CNN NILM Model"]

&nbsp;   LSTM\["LSTM/GRU Forecasting Model"]



&nbsp;   %% Outputs

&nbsp;   OUT\_CNN\["NILM Outputs<br/>Appliance ON/OFF"]

&nbsp;   OUT\_LSTM\["Forecast Outputs<br/>Next‑hour usage"]



&nbsp;   %% Dashboard

&nbsp;   DASH\["Tableau Dashboard<br/>Status • Summary • ML Insights"]



&nbsp;   %% Connections

&nbsp;   RAW --> INGEST --> CLEAN --> RESAMPLE --> SLICE --> PROC

&nbsp;   PROC --> WIN\_CNN --> CNN --> OUT\_CNN --> DASH

&nbsp;   PROC --> WIN\_LSTM --> LSTM --> OUT\_LSTM --> DASH




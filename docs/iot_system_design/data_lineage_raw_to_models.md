flowchart LR



&nbsp;   %% Raw Layer

&nbsp;   subgraph RAW\["Raw Layer"]

&nbsp;       RAW\_HDF5\["Raw UK‑DALE HDF5 Files"]

&nbsp;       RAW\_STREAM\["MQTT Raw Stream Messages"]

&nbsp;   end



&nbsp;   %% Validation Layer

&nbsp;   subgraph VALID\["Validation Layer"]

&nbsp;       SCHEMA\["Schema Validation"]

&nbsp;       RANGE\["Range Checks"]

&nbsp;       MISSING\["Missing Value Detection"]

&nbsp;       DUP\["Duplicate Timestamp Removal"]

&nbsp;   end



&nbsp;   %% Cleaning Layer

&nbsp;   subgraph CLEAN\["Cleaning Layer"]

&nbsp;       DROP\_ZERO\["Drop Zero/Corrupt Values"]

&nbsp;       CLIP\["Clip Outliers"]

&nbsp;       INTERP\["Interpolation for Gaps"]

&nbsp;       ALIGN\["Timestamp Alignment (UTC)"]

&nbsp;   end



&nbsp;   %% Resampling Layer

&nbsp;   subgraph RESAMP\["Resampling Layer"]

&nbsp;       RESAMPLE\_1M\["1‑Minute Resampling"]

&nbsp;       AGG\["Aggregation (mean/sum)"]

&nbsp;       SYNC\["Cross‑House Synchronization"]

&nbsp;   end



&nbsp;   %% Feature Layer

&nbsp;   subgraph FEAT\["Feature Engineering Layer"]

&nbsp;       WIN\_CNN\["Sliding Windows for CNN"]

&nbsp;       WIN\_LSTM\["Sequence Windows for LSTM"]

&nbsp;       NORM\["Normalization / Scaling"]

&nbsp;   end



&nbsp;   %% Model Inputs

&nbsp;   subgraph MODEL\_IN\["Model Input Layer"]

&nbsp;       CNN\_INPUT\["CNN Input Tensors"]

&nbsp;       LSTM\_INPUT\["LSTM Input Sequences"]

&nbsp;   end



&nbsp;   %% Models

&nbsp;   subgraph MODELS\["Model Layer"]

&nbsp;       CNN\["CNN NILM Model"]

&nbsp;       LSTM\["LSTM/GRU Forecasting Model"]

&nbsp;   end



&nbsp;   %% Outputs

&nbsp;   subgraph OUTPUTS\["Output Layer"]

&nbsp;       NILM\_OUT\["NILM Appliance Events"]

&nbsp;       FORECAST\_OUT\["Next‑Hour Forecast Values"]

&nbsp;   end



&nbsp;   %% Dashboard

&nbsp;   subgraph DASH\["Dashboard Layer"]

&nbsp;       TBL\["Tableau Dashboard"]

&nbsp;   end



&nbsp;   %% Connections

&nbsp;   RAW\_HDF5 --> SCHEMA

&nbsp;   RAW\_STREAM --> SCHEMA



&nbsp;   SCHEMA --> RANGE --> MISSING --> DUP --> DROP\_ZERO --> CLIP --> INTERP --> ALIGN --> RESAMPLE\_1M --> AGG --> SYNC



&nbsp;   SYNC --> WIN\_CNN --> NORM --> CNN\_INPUT --> CNN --> NILM\_OUT --> TBL

&nbsp;   SYNC --> WIN\_LSTM --> NORM --> LSTM\_INPUT --> LSTM --> FORECAST\_OUT --> TBL




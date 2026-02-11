flowchart LR



&nbsp;   %% Raw Data

&nbsp;   RAW\["Raw UK‑DALE Data<br/>Irregular timestamps<br/>Multiple sampling rates"]



&nbsp;   %% Alignment

&nbsp;   subgraph ALIGN\["Timestamp Alignment"]

&nbsp;       TZ\["Convert to UTC"]

&nbsp;       SORT\["Sort by Timestamp"]

&nbsp;       DEDUP\["Remove Duplicate Timestamps"]

&nbsp;   end



&nbsp;   %% Resampling

&nbsp;   subgraph RESAMPLE\["Resampling Process"]

&nbsp;       FILL\["Forward/Linear Fill<br/>Handle gaps"]

&nbsp;       RESAMP\["Resample to 1‑Minute Interval"]

&nbsp;       AGG\["Aggregation<br/>Mean / Sum / Median"]

&nbsp;   end



&nbsp;   %% Synchronization

&nbsp;   subgraph SYNC\["Cross‑House Synchronization"]

&nbsp;       INTERSECT\["Find Common Time Range"]

&nbsp;       TRIM\["Trim to Shared Window<br/>(e.g., 180 days)"]

&nbsp;   end



&nbsp;   %% Output

&nbsp;   CLEAN\["Aligned \& Resampled Data<br/>1‑Minute CSVs<br/>House\_1\_cleaned.csv<br/>House\_2\_cleaned.csv"]



&nbsp;   %% Connections

&nbsp;   RAW --> TZ --> SORT --> DEDUP --> FILL --> RESAMP --> AGG --> INTERSECT --> TRIM --> CLEAN




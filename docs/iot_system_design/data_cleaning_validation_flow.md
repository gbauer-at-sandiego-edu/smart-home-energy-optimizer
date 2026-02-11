flowchart LR



&nbsp;   %% Raw Data

&nbsp;   RAW\["Raw UK‑DALE Data<br/>HDF5 (ukdale.h5)"]



&nbsp;   %% Validation

&nbsp;   subgraph VALIDATION\["Validation Checks"]

&nbsp;       SCHEMA\["Schema Check<br/>Correct fields?"]

&nbsp;       RANGE\["Range Check<br/>Power values valid?"]

&nbsp;       MISSING\["Missing Value Check"]

&nbsp;       DUP\["Duplicate Timestamp Check"]

&nbsp;   end



&nbsp;   %% Cleaning

&nbsp;   subgraph CLEANING\["Cleaning Operations"]

&nbsp;       DROP\_ZERO\["Drop Zero / Corrupt Readings"]

&nbsp;       CLIP\["Clip Outliers<br/>(e.g., > 20kW)"]

&nbsp;       INTERP\["Interpolation<br/>Linear fill for gaps"]

&nbsp;       ALIGN\["Timestamp Alignment<br/>UTC normalization"]

&nbsp;   end



&nbsp;   %% Resampling \& Slicing

&nbsp;   subgraph RESAMPLE\["Resampling \& Slicing"]

&nbsp;       RESAMP\["1‑Minute Resampling"]

&nbsp;       SLICE\["180‑Day Slice<br/>Aligned across houses"]

&nbsp;   end



&nbsp;   %% Output

&nbsp;   PROC\["Processed CSVs<br/>House\_1\_cleaned.csv<br/>House\_2\_cleaned.csv"]



&nbsp;   %% Connections

&nbsp;   RAW --> SCHEMA --> RANGE --> MISSING --> DUP --> DROP\_ZERO --> CLIP --> INTERP --> ALIGN --> RESAMP --> SLICE --> PROC




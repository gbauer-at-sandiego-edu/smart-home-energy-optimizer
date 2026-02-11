```mermaid

flowchart TD



&nbsp;   ROOT\["/ (RootGroup)"]



&nbsp;   %% Buildings

&nbsp;   ROOT --> B1\["building1"]

&nbsp;   ROOT --> B2\["building2"]

&nbsp;   ROOT --> B3\["building3"]

&nbsp;   ROOT --> B4\["building4"]

&nbsp;   ROOT --> B5\["building5"]



&nbsp;   %% Elec groups

&nbsp;   B1 --> B1E\["elec"]

&nbsp;   B2 --> B2E\["elec"]

&nbsp;   B3 --> B3E\["elec"]

&nbsp;   B4 --> B4E\["elec"]

&nbsp;   B5 --> B5E\["elec"]



&nbsp;   %% Representative meters only (GitHub cannot render all 111)

&nbsp;   B1E --> B1M1\["meter1"]

&nbsp;   B1E --> B1M2\["meter2"]

&nbsp;   B1E --> B1M3\["meter3"]

&nbsp;   B1E --> B1More\["… meter4–meter54"]



&nbsp;   B2E --> B2M1\["meter1"]

&nbsp;   B2E --> B2M2\["meter2"]

&nbsp;   B2E --> B2More\["… meter3–meter20"]



&nbsp;   B3E --> B3M1\["meter1"]

&nbsp;   B3E --> B3More\["… meter2–meter5"]



&nbsp;   B4E --> B4M1\["meter1"]

&nbsp;   B4E --> B4More\["… meter2–meter6"]



&nbsp;   B5E --> B5M1\["meter1"]

&nbsp;   B5E --> B5M2\["meter2"]

&nbsp;   B5E --> B5More\["… meter3–meter26"]



&nbsp;   %% Table nodes (representative only)

&nbsp;   B1M1 --> B1M1T\["table"]

&nbsp;   B2M1 --> B2M1T\["table"]

&nbsp;   B3M1 --> B3M1T\["table"]

&nbsp;   B4M1 --> B4M1T\["table"]

&nbsp;   B5M1 --> B5M1T\["table"]

```




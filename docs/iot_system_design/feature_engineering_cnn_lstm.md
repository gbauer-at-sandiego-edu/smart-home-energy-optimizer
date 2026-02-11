flowchart TB



&nbsp;   %% Input

&nbsp;   PROC\["Processed 1‑Minute Data<br/>House\_1\_cleaned.csv<br/>House\_2\_cleaned.csv"]



&nbsp;   %% CNN Branch

&nbsp;   subgraph CNN\_FE\["CNN NILM Feature Engineering"]

&nbsp;       NORM\_CNN\["Normalization<br/>Min‑Max or Standard Scaling"]

&nbsp;       WIN\_CNN\["Sliding Window Creation<br/>e.g., 128–512 timesteps"]

&nbsp;       LABEL\_CNN\["Label Extraction<br/>Appliance ON/OFF"]

&nbsp;       CNN\_INPUT\["CNN Input Tensors<br/>Shape: \[window, 1]"]

&nbsp;   end



&nbsp;   %% LSTM Branch

&nbsp;   subgraph LSTM\_FE\["LSTM/GRU Forecasting Feature Engineering"]

&nbsp;       NORM\_LSTM\["Normalization<br/>Scaling across full sequence"]

&nbsp;       WIN\_LSTM\["Sequence Windowing<br/>Past 24h → Next Hour"]

&nbsp;       TARGET\_LSTM\["Target Extraction<br/>Next‑hour usage"]

&nbsp;       LSTM\_INPUT\["LSTM Input Sequences<br/>Shape: \[1440, 1]"]

&nbsp;   end



&nbsp;   %% Connections

&nbsp;   PROC --> NORM\_CNN --> WIN\_CNN --> LABEL\_CNN --> CNN\_INPUT

&nbsp;   PROC --> NORM\_LSTM --> WIN\_LSTM --> TARGET\_LSTM --> LSTM\_INPUT




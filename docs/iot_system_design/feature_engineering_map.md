flowchart LR



&nbsp;   %% Raw Inputs

&nbsp;   subgraph RAW\["Raw Inputs"]

&nbsp;       POWER\["Power (W)"]

&nbsp;       VOLT\["Voltage (V)"]

&nbsp;       CURR\["Current (A)"]

&nbsp;       FREQ\["Frequency (Hz)"]

&nbsp;       TIME\["Timestamp"]

&nbsp;   end



&nbsp;   %% Preprocessing

&nbsp;   subgraph PREP\["Preprocessing"]

&nbsp;       CLEAN\["Cleaning<br/>Missing values • Outlier removal"]

&nbsp;       ALIGN\["Time Alignment<br/>1‑min windows"]

&nbsp;       NORM\["Normalization / Scaling"]

&nbsp;   end



&nbsp;   %% Feature Engineering

&nbsp;   subgraph FEAT\["Engineered Features"]

&nbsp;       ROLL\_MEAN\["Rolling Mean<br/>1m • 5m • 15m"]

&nbsp;       ROLL\_STD\["Rolling Std Dev"]

&nbsp;       DIFF\["First Differences"]

&nbsp;       LAGS\["Lag Features<br/>t‑1 • t‑2 • t‑3"]

&nbsp;       PEAKS\["Peak Detection"]

&nbsp;       TIME\_FEATS\["Time Features<br/>Hour • Day • Weekend"]

&nbsp;   end



&nbsp;   %% Model Inputs

&nbsp;   subgraph CNN\["CNN NILM Model Inputs"]

&nbsp;       CNN\_WIN\["Sliding Windows<br/>Raw + normalized signals"]

&nbsp;       CNN\_SHAPE\["Window Shape<br/>\[window\_size × channels]"]

&nbsp;   end



&nbsp;   subgraph LSTM\["LSTM Forecast Model Inputs"]

&nbsp;       LSTM\_SEQ\["Sequences<br/>Lagged power usage"]

&nbsp;       LSTM\_FEATS\["Feature Vector<br/>Rolling stats + time features"]

&nbsp;   end



&nbsp;   %% Connections

&nbsp;   POWER --> CLEAN

&nbsp;   VOLT --> CLEAN

&nbsp;   CURR --> CLEAN

&nbsp;   FREQ --> CLEAN

&nbsp;   TIME --> ALIGN



&nbsp;   CLEAN --> ALIGN --> NORM



&nbsp;   NORM --> ROLL\_MEAN

&nbsp;   NORM --> ROLL\_STD

&nbsp;   NORM --> DIFF

&nbsp;   NORM --> LAGS

&nbsp;   NORM --> PEAKS

&nbsp;   TIME --> TIME\_FEATS



&nbsp;   %% CNN Inputs

&nbsp;   NORM --> CNN\_WIN --> CNN\_SHAPE



&nbsp;   %% LSTM Inputs

&nbsp;   ROLL\_MEAN --> LSTM\_FEATS

&nbsp;   ROLL\_STD --> LSTM\_FEATS

&nbsp;   DIFF --> LSTM\_FEATS

&nbsp;   LAGS --> LSTM\_SEQ

&nbsp;   TIME\_FEATS --> LSTM\_FEATS




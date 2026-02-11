flowchart TB



&nbsp;   %% Input Data

&nbsp;   PROC\["Processed 1‑Minute Data<br/>Cleaned CSVs"]



&nbsp;   %% Feature Engineering

&nbsp;   subgraph FEAT\["Feature Engineering"]

&nbsp;       WIN\_CNN\["CNN Sliding Windows"]

&nbsp;       WIN\_LSTM\["LSTM Sequence Windows"]

&nbsp;       NORM\["Normalization / Scaling"]

&nbsp;   end



&nbsp;   %% CNN Training Pipeline

&nbsp;   subgraph CNN\_PIPE\["CNN NILM Training Pipeline"]

&nbsp;       BATCH\_CNN\["Batching<br/>Window batches"]

&nbsp;       TRAIN\_CNN\["Training Loop<br/>Forward + Backprop"]

&nbsp;       VAL\_CNN\["Validation Loop<br/>Accuracy • F1"]

&nbsp;       CHECK\_CNN\["Model Checkpoint<br/>Best weights"]

&nbsp;       SAVE\_CNN\["Save Trained CNN Model"]

&nbsp;   end



&nbsp;   %% LSTM Training Pipeline

&nbsp;   subgraph LSTM\_PIPE\["LSTM/GRU Forecasting Training Pipeline"]

&nbsp;       BATCH\_LSTM\["Batching<br/>Sequence batches"]

&nbsp;       TRAIN\_LSTM\["Training Loop<br/>Forward + Backprop"]

&nbsp;       VAL\_LSTM\["Validation Loop<br/>MAE • RMSE"]

&nbsp;       CHECK\_LSTM\["Model Checkpoint<br/>Best weights"]

&nbsp;       SAVE\_LSTM\["Save Trained LSTM Model"]

&nbsp;   end



&nbsp;   %% Connections

&nbsp;   PROC --> WIN\_CNN --> NORM --> BATCH\_CNN --> TRAIN\_CNN --> VAL\_CNN --> CHECK\_CNN --> SAVE\_CNN

&nbsp;   PROC --> WIN\_LSTM --> NORM --> BATCH\_LSTM --> TRAIN\_LSTM --> VAL\_LSTM --> CHECK\_LSTM --> SAVE\_LSTM




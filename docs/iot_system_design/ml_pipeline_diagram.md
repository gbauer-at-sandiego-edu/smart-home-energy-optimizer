flowchart LR

&nbsp;   %% Processed Data

&nbsp;   PROC\["Processed 1‑Minute Data<br/>House\_1\_cleaned.csv<br/>House\_2\_cleaned.csv"]



&nbsp;   %% CNN Branch

&nbsp;   subgraph CNN\_Pipeline\["CNN NILM Pipeline"]

&nbsp;       direction LR

&nbsp;       WIN\_CNN\["Windowing<br/>(Sliding windows of mains power)"]

&nbsp;       PREP\_CNN\["Normalization<br/>Train/Val Split"]

&nbsp;       MODEL\_CNN\["CNN Model<br/>Conv1D → MaxPool → Conv1D → GAP → Dense"]

&nbsp;       TRAIN\_CNN\["Training Loop<br/>Early Stopping + Checkpoints"]

&nbsp;       EVAL\_CNN\["Evaluation<br/>Accuracy • F1 • Confusion Matrix"]

&nbsp;       OUT\_CNN\["NILM Outputs<br/>Appliance ON/OFF"]

&nbsp;   end



&nbsp;   %% LSTM Branch

&nbsp;   subgraph LSTM\_Pipeline\["LSTM Forecasting Pipeline"]

&nbsp;       direction LR

&nbsp;       WIN\_LSTM\["Sequence Windowing<br/>(Past 24h → Next Hour)"]

&nbsp;       PREP\_LSTM\["Normalization<br/>Train/Val Split"]

&nbsp;       MODEL\_LSTM\["LSTM/GRU Model<br/>Sequence-to-One"]

&nbsp;       TRAIN\_LSTM\["Training Loop<br/>Early Stopping + Checkpoints"]

&nbsp;       EVAL\_LSTM\["Evaluation<br/>MAE • RMSE • Forecast Plots"]

&nbsp;       OUT\_LSTM\["Forecast Outputs<br/>Next‑Hour Usage"]

&nbsp;   end



&nbsp;   %% Dashboard

&nbsp;   DASH\["Tableau Dashboard<br/>NILM Insight • Forecast Insight"]



&nbsp;   %% Connections

&nbsp;   PROC --> WIN\_CNN --> PREP\_CNN --> MODEL\_CNN --> TRAIN\_CNN --> EVAL\_CNN --> OUT\_CNN --> DASH

&nbsp;   PROC --> WIN\_LSTM --> PREP\_LSTM --> MODEL\_LSTM --> TRAIN\_LSTM --> EVAL\_LSTM --> OUT\_LSTM --> DASH




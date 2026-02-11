flowchart TB



&nbsp;   %% Dataset Split

&nbsp;   subgraph SPLIT\["Dataset Split"]

&nbsp;       TRAIN\["Training Set<br/>70%"]

&nbsp;       VAL\["Validation Set<br/>15%"]

&nbsp;       TEST\["Test Set<br/>15%"]

&nbsp;   end



&nbsp;   %% CNN Metrics

&nbsp;   subgraph CNN\_METRICS\["CNN NILM Evaluation"]

&nbsp;       ACC\["Accuracy"]

&nbsp;       PREC\["Precision"]

&nbsp;       REC\["Recall"]

&nbsp;       F1\["F1 Score"]

&nbsp;       CONF\["Confusion Matrix"]

&nbsp;   end



&nbsp;   %% LSTM Metrics

&nbsp;   subgraph LSTM\_METRICS\["LSTM Forecasting Evaluation"]

&nbsp;       MAE\["MAE<br/>(Mean Absolute Error)"]

&nbsp;       RMSE\["RMSE<br/>(Root Mean Square Error)"]

&nbsp;       MAPE\["MAPE<br/>(% Error)"]

&nbsp;       CURVE\["Predicted vs Actual Curve"]

&nbsp;   end



&nbsp;   %% Validation Flow

&nbsp;   subgraph FLOW\["Validation Flow"]

&nbsp;       TRAIN\_LOOP\["Training Loop"]

&nbsp;       VAL\_LOOP\["Validation Loop"]

&nbsp;       EARLY\_STOP\["Early Stopping<br/>Monitor val\_loss"]

&nbsp;       CHECKPOINT\["Model Checkpoint<br/>Best weights saved"]

&nbsp;       FINAL\_EVAL\["Final Evaluation on Test Set"]

&nbsp;   end



&nbsp;   %% Connections

&nbsp;   TRAIN --> TRAIN\_LOOP --> VAL\_LOOP --> EARLY\_STOP --> CHECKPOINT --> FINAL\_EVAL

&nbsp;   VAL --> VAL\_LOOP

&nbsp;   TEST --> FINAL\_EVAL



&nbsp;   FINAL\_EVAL --> ACC

&nbsp;   FINAL\_EVAL --> PREC

&nbsp;   FINAL\_EVAL --> REC

&nbsp;   FINAL\_EVAL --> F1

&nbsp;   FINAL\_EVAL --> CONF



&nbsp;   FINAL\_EVAL --> MAE

&nbsp;   FINAL\_EVAL --> RMSE

&nbsp;   FINAL\_EVAL --> MAPE

&nbsp;   FINAL\_EVAL --> CURVE




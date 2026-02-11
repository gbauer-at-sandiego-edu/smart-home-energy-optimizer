sequenceDiagram

&nbsp;   autonumber



&nbsp;   participant TSDB as Time‑Series DB<br/>(1‑min curated data)

&nbsp;   participant CNN as CNN NILM Model

&nbsp;   participant LSTM as LSTM/GRU Forecasting Model

&nbsp;   participant DASH as Tableau Dashboard



&nbsp;   %% CNN NILM Inference

&nbsp;   TSDB->>CNN: Provide sliding window<br/>(mains power sequence)

&nbsp;   CNN->>CNN: Run Conv1D inference<br/>Detect appliance signatures

&nbsp;   CNN->>TSDB: Store NILM output<br/>(ON/OFF events)

&nbsp;   CNN->>DASH: Send appliance breakdown<br/>(per‑minute)



&nbsp;   %% LSTM Forecasting Inference

&nbsp;   TSDB->>LSTM: Provide past 24 hours<br/>(sequence window)

&nbsp;   LSTM->>LSTM: Run LSTM/GRU inference<br/>Predict next hour usage

&nbsp;   LSTM->>TSDB: Store forecast results<br/>(predicted values)

&nbsp;   LSTM->>DASH: Send forecast curve<br/>(predicted vs actual)



&nbsp;   %% Dashboard Rendering

&nbsp;   DASH->>DASH: Render visualizations<br/>Status • Summary • ML Insights




flowchart TB



&nbsp;   %% Input

&nbsp;   INPUT\["Input Sequence<br/>(Past 24 hours)<br/>Shape: \[1440 timesteps, 1 feature]"]



&nbsp;   %% LSTM/GRU Block

&nbsp;   subgraph RNN\_BLOCK\["Recurrent Block"]

&nbsp;       LSTM1\["LSTM Layer<br/>Units: 64<br/>Return sequences: True"]

&nbsp;       LSTM2\["LSTM Layer<br/>Units: 32<br/>Return sequences: False"]

&nbsp;       DROPOUT\["Dropout<br/>Rate: 0.2"]

&nbsp;   end



&nbsp;   %% Dense Layers

&nbsp;   subgraph DENSE\["Dense Layers"]

&nbsp;       D1\["Dense Layer<br/>Units: 32<br/>ReLU"]

&nbsp;       D2\["Dense Layer<br/>Units: 16<br/>ReLU"]

&nbsp;       OUT\["Output Layer<br/>1 value<br/>(Next‑hour forecast)"]

&nbsp;   end



&nbsp;   %% Connections

&nbsp;   INPUT --> LSTM1 --> LSTM2 --> DROPOUT --> D1 --> D2 --> OUT




flowchart TB



&nbsp;   %% Input

&nbsp;   INPUT\["Input Window<br/>(e.g., 128–512 timesteps)<br/>1D mains power sequence"]



&nbsp;   %% Conv Block 1

&nbsp;   subgraph BLOCK1\["Conv Block 1"]

&nbsp;       CONV1\["Conv1D<br/>Filters: 32<br/>Kernel: 3"]

&nbsp;       RELU1\["ReLU Activation"]

&nbsp;       POOL1\["MaxPool1D<br/>Pool size: 2"]

&nbsp;   end



&nbsp;   %% Conv Block 2

&nbsp;   subgraph BLOCK2\["Conv Block 2"]

&nbsp;       CONV2\["Conv1D<br/>Filters: 64<br/>Kernel: 3"]

&nbsp;       RELU2\["ReLU Activation"]

&nbsp;       POOL2\["MaxPool1D<br/>Pool size: 2"]

&nbsp;   end



&nbsp;   %% Conv Block 3

&nbsp;   subgraph BLOCK3\["Conv Block 3"]

&nbsp;       CONV3\["Conv1D<br/>Filters: 128<br/>Kernel: 3"]

&nbsp;       RELU3\["ReLU Activation"]

&nbsp;       GAP\["Global Average Pooling"]

&nbsp;   end



&nbsp;   %% Dense Layers

&nbsp;   subgraph DENSE\["Dense Layers"]

&nbsp;       D1\["Dense Layer<br/>Units: 64<br/>ReLU"]

&nbsp;       D2\["Dense Layer<br/>Units: 32<br/>ReLU"]

&nbsp;       OUT\["Output Layer<br/>Sigmoid (ON/OFF)"]

&nbsp;   end



&nbsp;   %% Connections

&nbsp;   INPUT --> CONV1 --> RELU1 --> POOL1 --> CONV2 --> RELU2 --> POOL2 --> CONV3 --> RELU3 --> GAP --> D1 --> D2 --> OUT




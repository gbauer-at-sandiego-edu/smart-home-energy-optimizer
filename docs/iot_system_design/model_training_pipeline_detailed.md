flowchart TB



&nbsp;   %% Data Extraction

&nbsp;   subgraph EXTRACT\["Data Extraction"]

&nbsp;       PULL\_TSDB\["Pull Curated Data<br/>TSDB (1‑min aligned)"]

&nbsp;       PULL\_OBJ\["Pull Raw/Processed Files<br/>Object Storage"]

&nbsp;       MERGE\["Merge Sources<br/>Align timestamps + house\_id"]

&nbsp;   end



&nbsp;   %% Data Preparation

&nbsp;   subgraph PREP\["Data Preparation"]

&nbsp;       CLEAN\["Cleaning<br/>Missing values • Outlier removal"]

&nbsp;       RESAMPLE\["Resampling<br/>1‑min → model‑ready windows"]

&nbsp;       FEAT\_ENG\["Feature Engineering<br/>Lag features • Rolling stats"]

&nbsp;       SPLIT\["Train/Validation/Test Split"]

&nbsp;   end



&nbsp;   %% Training

&nbsp;   subgraph TRAIN\["Model Training"]

&nbsp;       CNN\_TRAIN\["Train CNN NILM Model"]

&nbsp;       LSTM\_TRAIN\["Train LSTM Forecast Model"]

&nbsp;       HP\_TUNE\["Hyperparameter Tuning<br/>Grid/Random/Bayesian"]

&nbsp;   end



&nbsp;   %% Evaluation

&nbsp;   subgraph EVAL\["Model Evaluation"]

&nbsp;       METRICS\["Compute Metrics<br/>MAE • RMSE • F1 • Accuracy"]

&nbsp;       THRESH\["Threshold Optimization<br/>NILM ON/OFF cutoff"]

&nbsp;       COMPARE\["Compare Against Baselines"]

&nbsp;   end



&nbsp;   %% Versioning \& Registry

&nbsp;   subgraph REG\["Versioning \& Registry"]

&nbsp;       VERSION\["Assign Version<br/>Model vX.Y.Z"]

&nbsp;       SAVE\_ARTIFACTS\["Save Artifacts<br/>Weights • Config • Metrics"]

&nbsp;       REGISTER\["Register in Model Registry"]

&nbsp;   end



&nbsp;   %% Deployment

&nbsp;   subgraph DEPLOY\["Deployment"]

&nbsp;       BATCH\_JOB\["Deploy Batch Prediction Job"]

&nbsp;       DASH\_SYNC\["Sync Outputs to Dashboard"]

&nbsp;   end



&nbsp;   %% Connections

&nbsp;   PULL\_TSDB --> MERGE

&nbsp;   PULL\_OBJ --> MERGE

&nbsp;   MERGE --> CLEAN --> RESAMPLE --> FEAT\_ENG --> SPLIT



&nbsp;   SPLIT --> CNN\_TRAIN

&nbsp;   SPLIT --> LSTM\_TRAIN

&nbsp;   CNN\_TRAIN --> HP\_TUNE

&nbsp;   LSTM\_TRAIN --> HP\_TUNE



&nbsp;   HP\_TUNE --> METRICS --> THRESH --> COMPARE



&nbsp;   COMPARE --> VERSION --> SAVE\_ARTIFACTS --> REGISTER



&nbsp;   REGISTER --> BATCH\_JOB --> DASH\_SYNC




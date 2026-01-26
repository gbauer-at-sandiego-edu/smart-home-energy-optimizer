```mermaid
flowchart TD

    %% ============================
    %% Global Dataset Metadata
    %% ============================
    A[dataset.txt<br/>• name<br/>• number_of_buildings<br/>• timeframe<br/>• timezone] 

    %% ============================
    %% Building Metadata
    %% ============================
    A --> B1[buildingN.txt<br/>• building_type<br/>• construction_year<br/>• occupants<br/>• appliances[]<br/>• elec_meters{}]

    %% ============================
    %% Appliances
    %% ============================
    B1 --> C[appliances[]<br/>• type<br/>• meters[]<br/>• room<br/>• description<br/>• dates_active]

    %% ============================
    %% Meters
    %% ============================
    B1 --> D[elec_meters{}<br/>• meter_id<br/>• data_location<br/>• device_model<br/>• site_meter<br/>• submeter_of<br/>• timeframe]

    %% ============================
    %% Meter Devices
    %% ============================
    D --> E[meter_devices.txt<br/>• sample_period<br/>• measurements<br/>• wireless<br/>• model_url]

    %% ============================
    %% Raw Data Files
    %% ============================
    D --> F[house_N folder<br/>data/raw/house_N/]

    F --> G[channel_X.dat<br/>• timestamp<br/>• power]

    F --> H[mains.dat<br/>• timestamp<br/>• power]

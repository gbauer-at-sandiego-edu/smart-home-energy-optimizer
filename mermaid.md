```mermaid
flowchart TD

    %% ============================
    %% Global Dataset Metadata
    %% ============================
    A["dataset.txt
    name
    number_of_buildings
    timeframe
    timezone"]

    %% ============================
    %% Building Metadata
    %% ============================
    A --> B1["buildingN.txt
    building_type
    construction_year
    occupants
    appliances[]
    elec_meters{}"]

    %% ============================
    %% Appliances
    %% ============================
    B1 --> C["appliances[]
    type
    meters[]
    room
    description
    dates_active"]

    %% ============================
    %% Meters
    %% ============================
    B1 --> D["elec_meters{}
    meter_id
    data_location
    device_model
    site_meter
    submeter_of
    timeframe"]

    %% ============================
    %% Meter Devices
    %% ============================
    D --> E["meter_devices.txt
    sample_period
    measurements
    wireless
    model_url"]

    %% ============================
    %% Raw Data Files
    %% ============================
    D --> F["house_N folder
    data/raw/house_N/"]

    F --> G["channel_X.dat
    timestamp
    power"]

    F --> H["mains.dat
    timestamp
    power"]


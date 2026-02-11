---
config:
  layout: elk
---
flowchart TB
 subgraph Home["Home"]
        SM["Smart Meter\nMain Power"]
        CT1["CT Clamp Sensors\nCircuits/Appliances"]
        ENV["Environmental Sensors\nTemp, Humidity, Light"]
        GW["Edge Gateway\n(Raspberry Pi / Router)"]
  end
 subgraph Network["Network"]
        WIFI["Wi-Fi / Ethernet"]
        MQTT["MQTT over TLS"]
  end
 subgraph Cloud["Cloud"]
        LB["API Gateway / Load Balancer"]
        ING["Ingestion Service\n(MQTT bridge / REST)"]
        KAFKA["Stream Bus\n(Kafka / IoT Hub)"]
        TSDB["Time-Series DB\n(InfluxDB / TimescaleDB)"]
        DATALAKE["Data Lake\n(Object Storage)"]
        FEAT["Feature Pipeline\n(Batch / Streaming)"]
        MLTRAIN["Model Training\n(LSTM / TFT)"]
        MLSERVE["Model Serving API"]
        DASH["Dashboard & Automation Engine"]
  end
    SM -- kWh, kW, voltage --> GW
    CT1 -- "circuit-level watts" --> GW
    ENV -- temp, humidity --> GW
    GW -- MQTT --> WIFI
    WIFI --> MQTT
    MQTT --> LB
    LB --> ING
    ING --> KAFKA
    KAFKA --> TSDB & DATALAKE
    TSDB --> FEAT & DASH
    FEAT --> MLTRAIN & MLSERVE
    MLSERVE --> DASH
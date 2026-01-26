# UK‑DALE Dataset — Data Dictionary & Schema

This document provides a structured overview of the UK‑DALE dataset as used in this project, including file formats, metadata structure, and relationships between buildings, meters, appliances, and raw time‑series data.

---

## 1. Time‑Series Files (`.dat`)

Each `.dat` file is a space‑separated CSV with no header.

### File Format
| Column      | Type     | Description                                      |
|-------------|----------|--------------------------------------------------|
| timestamp   | int64    | UNIX timestamp (seconds, UTC)                    |
| power       | float32  | Power reading in watts                           |

### Notes
- Sampling period is typically **6 seconds** (EcoManager / CurrentCost).
- Some mains meters use **1‑second** sampling (SoundCardPowerMeter).
- In analysis, timestamps are converted to a timezone‑aware `DatetimeIndex`.

---

## 2. Building Metadata (`building1.txt` … `building5.txt`)

Each file describes one building.

### Top‑Level Fields
| Field                    | Type   | Description |
|--------------------------|--------|-------------|
| building_type            | string | e.g., *end of terrace*, *flat* |
| construction_year        | int    | Year the home was built |
| description_of_occupants | string | Household composition |
| appliances               | list   | Appliance metadata entries |
| elec_meters              | dict   | Meter metadata entries |

---

## 2.1 Appliance Metadata

Each appliance entry contains:

| Field            | Type        | Description |
|------------------|-------------|-------------|
| type             | string      | Appliance category (e.g., kettle, fridge) |
| original_name    | string      | Name used during data collection |
| meters           | list[int]   | Meter IDs associated with this appliance |
| room             | string      | Location in the home |
| year_of_purchase | int         | Optional |
| description      | string      | Free‑text notes |
| dates_active     | list        | Optional start/end periods |
| components       | list        | Optional subcomponents |

---

## 2.2 Meter Metadata

Each meter entry is keyed by meter ID:

| Field         | Type   | Description |
|---------------|--------|-------------|
| data_location | string | Path to `.dat` file (e.g., `house_1/channel_10.dat`) |
| device_model  | string | Meter type (e.g., EcoManagerTxPlug) |
| site_meter    | bool   | True if this is the mains meter |
| submeter_of   | int    | Parent meter ID (0 = none) |
| disabled      | bool   | True if meter was inactive |
| timeframe     | dict   | `{start: ISO8601, end: ISO8601}` |

---

## 3. Dataset Metadata (`dataset.txt`)

Global dataset‑level information.

| Field               | Type   | Description |
|---------------------|--------|-------------|
| name                | string | Dataset name (UK‑DALE) |
| description         | string | High‑level summary |
| number_of_buildings | int    | Always 5 |
| geo_location        | dict   | Latitude/longitude |
| timeframe           | dict   | Global start/end timestamps |
| timezone            | string | Europe/London |
| creators            | list   | Dataset authors |
| related_documents   | list   | Publications and links |

---

## 4. Meter Device Metadata (`meter_devices.txt`)

Defines sampling periods and measurement capabilities for each meter type.

| Field            | Type   | Description |
|------------------|--------|-------------|
| sample_period    | int    | Sampling interval in seconds |
| measurements     | list   | Power/voltage measurement specs |
| max_sample_period| int    | Maximum supported interval |
| wireless         | bool   | Whether the meter is wireless |
| model_url        | string | Documentation link |

---

## 5. Dataset Schema Diagram (ASCII)
┌──────────────────────────────┐
│        dataset.txt           │
│  - name                      │
│  - number_of_buildings       │
│  - timeframe                 │
│  - timezone                  │
└───────────────┬──────────────┘
                │
                ▼
┌──────────────────────────────────────────┐
│           buildingN.txt                  │
│  - building_type                         │
│  - construction_year                     │
│  - description_of_occupants              │
│  - appliances[]                          │
│  - elec_meters{}                         │
└───────────────┬──────────────────────────┘
                           │
┌──────────────────────────┼──────────────────────────┐
▼                          ▼                          ▼
┌──────────────────┐     ┌──────────────────┐        ┌──────────────────┐
│   appliances[]   │     │  elec_meters{}   │        │ meter_devices.txt│
│ - type           │     │ - meter_id       │        │ - sample_period  │
│ - meters[]       │     │ - data_location  │        │ - measurements   │
│ - room           │     │ - device_model   │        │ - device specs   │
│ - dates_active   │     │ - site_meter     │        └──────────────────┘
└─────────┬────────┘     │ - timeframe      │
          │              └─────────┬────────┘
          │                        │
          ▼                        ▼
┌──────────────────┐     ┌──────────────────────────────┐
│  house_N folder   │     │   channel_X.dat / mains.dat  │
│  (data/raw/)      │────▶│   timestamp, power           │
└──────────────────┘     └──────────────────────────────┘

---

## 6. Summary

This schema provides a complete reference for:

- Navigating the dataset  
- Understanding meter/appliance relationships  
- Interpreting raw `.dat` files  
- Using metadata to enrich analysis  

It is intended for new team members onboarding to the project.

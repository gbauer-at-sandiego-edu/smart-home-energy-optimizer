---

# **UK‑DALE HDF5 Dataset — Project Data Dictionary & Schema**

This document provides a complete, project‑specific description of the UK‑DALE dataset as stored in the NILMTK‑formatted HDF5 file (`ukdale.h5`).  
It reflects the **actual structure discovered through programmatic exploration**, including buildings, meters, table schemas, sampling intervals, and raw data fields.

---

# **1. Overview**

The dataset consists of **five residential buildings**, each containing multiple electricity meters.  
All data is stored in a hierarchical HDF5 structure using PyTables.  
Each meter contains a single table of raw power readings sampled at **6‑second intervals**.

This data dictionary describes:

- The HDF5 hierarchy  
- Meter schemas  
- Sampling characteristics  
- Row counts per meter  
- Example raw data  
- Notes relevant to preprocessing and modeling  

---

# **2. HDF5 File Structure**

The root of the file contains one group per building:

```
/building1
/building2
/building3
/building4
/building5
```

Each building contains an `elec` group:

```
/buildingX/elec/
```

Each meter is stored as:

```
/buildingX/elec/meterY/table
```

Example:

```
/building1/elec/meter1/table
```

---

# **3. Meter Table Schema**

Every meter table in the dataset shares the same schema:

| Column            | Type      | Description |
|-------------------|-----------|-------------|
| `index`           | int64     | Nanosecond UNIX timestamp |
| `values_block_0`  | float32   | Active power in watts |

Example PyTables description:

```
{
  "index": Int64Col(),
  "values_block_0": Float32Col(shape=(1,))
}
```

There are **no additional fields** such as voltage, current, temperature, or appliance labels.

---

# **4. Sampling Interval**

Using the first 50,000 samples of `building1/meter1`, the sampling interval was computed as:

- **Mode:** 6 seconds  
- **Median:** 6 seconds  

This matches the expected sampling rate of the EcoManager / CurrentCost meters used in UK‑DALE.

All meters examined follow the same 6‑second sampling pattern.

---

# **5. Meter Counts per Building**

Programmatic enumeration of the file revealed:

| Building   | Number of Meters |
|------------|------------------|
| building1  | 54 |
| building2  | 20 |
| building3  | 5 |
| building4  | 6 |
| building5  | 26 |

These counts match the NILMTK HDF5 format, where each appliance or circuit may have its own meter.

---

# **6. Row Counts per Meter**

Each meter contains a different number of rows depending on:

- duration of monitoring  
- sampling continuity  
- whether the meter was active for the full dataset period  

Examples:

- `building1/meter1`: **21,837,636 rows**  
- `building1/meter54`: **128,238,700 rows**  
- `building2/meter20`: **12,166,699 rows**  
- `building3/meter1`: **512,327 rows**  
- `building5/meter26`: **11,405,812 rows**

All meters contain only the two raw fields described above.

A full programmatic summary is available in the exploration notebook.

---

# **7. Example Raw Data**

Sample from `building1/meter1`:

| index (ns)           | values_block_0 |
|----------------------|----------------|
| 1352500095000000000  | 599.0          |
| 1352500101000000000  | 582.0          |
| 1352500107000000000  | 600.0          |
| 1352500113000000000  | 586.0          |
| 1352500120000000000  | 596.0          |

After conversion:

- `index` → UTC timestamp  
- `values_block_0` → `power_watts`  

---

# **8. Preprocessing Notes**

Before modeling, the following transformations were applied:

- Convert `index` from nanoseconds → timezone‑aware `DatetimeIndex`  
- Rename `values_block_0` → `power_watts`  
- Set timestamp as index  
- Resample to **1‑hour mean**  
- Remove negative or missing values  
- Engineer additional features (lags, rolling windows, calendar features)

These engineered features are **not part of the raw dataset**.

---

# **9. What the Dataset Does *Not* Contain**

The HDF5 file does **not** include:

- Appliance metadata  
- Building metadata  
- Environmental sensors (temperature, humidity, occupancy)  
- Voltage, current, or power factor  
- Labels for appliance usage  
- Any non‑electrical measurements  

All contextual and calendar features used in modeling were derived during preprocessing.

---

# **10. Summary**

This project uses the NILMTK HDF5 version of UK‑DALE, which provides:

- High‑resolution (6‑second) whole‑home and submetered power data  
- Five buildings with a total of 111 meters  
- A consistent two‑column schema across all meters  
- Large, continuous time‑series suitable for forecasting and NILM tasks  

This data dictionary reflects the **actual structure** of the dataset as verified through programmatic exploration.

---
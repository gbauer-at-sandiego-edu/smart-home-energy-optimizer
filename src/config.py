# src/config.py

BUILDING = 1

# UK-DALE (HDF5) keys inside ukdale.h5
MAINS_KEY = "/building1/elec/meter1"

# Start with meter13 (you may change this to meter14 after checking ON counts)
KETTLE_KEY = "/building1/elec/meter13"

# Modeling choices (Week 1)
RESAMPLE_RULE = "1min"
DAYS_TO_USE = 180
KETTLE_ON_THRESHOLD_W = 200

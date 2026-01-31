# How to Run Data Ingestion (UK-DALE) — Week 1

This project uses the UK-DALE dataset (Kaggle mirror HDF5: `ukdale.h5`) and produces a manageable 1-minute processed dataset slice for modeling.

## Prereqs
- Google Colab
- This GitHub repo cloned into Colab

## Steps (Colab)

### 1) Clone the repository and cd into it
```bash
!git clone https://github.com/gbauer-at-sandiego-edu/smart-home-energy-optimizer.git
%cd smart-home-energy-optimizer/smart-home-energy-optimizer/smart-home-energy-optimizer

!pip -q install kagglehub pandas tables

!PYTHONPATH=. python src/data_ingest.py


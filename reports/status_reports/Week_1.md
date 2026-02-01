\# Week 1 Status Report  

\*\*Team 2 – Smart Home Energy Optimizer\*\*  

\*\*AAI‑530: Data Analytics and the Internet of Things\*\*  

\*\*Reporting Period:\*\* January 28 – February 3, 2026



---



\## 1. Overview



Week 1 focused on establishing the foundation for the Smart Home Energy Optimizer project. The team completed dataset selection, exploratory data analysis, initial repository setup, and the required written responses addressing scalability and model selection. All core Week 1 deliverables were completed on schedule.



---



\## 2. Completed Deliverables



\### 2.1 Dataset Selection

\- Evaluated Houses 1, 2, and 5 using a structured decision matrix.

\- Selected Houses 1 and 2 based on recording duration, data quality, appliance coverage, and suitability for both NILM and forecasting.

\- Added summary, data slice selection, channel selection, and limitations sections to `dataset\_selection.md`.



\### 2.2 Exploratory Data Analysis (EDA)

\- Loaded and inspected mains and appliance‑level data.

\- Assessed missingness, sampling frequency, and channel availability.

\- Produced initial plots showing usage patterns and data quality.

\- Established a clean 1‑minute resampled subset for modeling.



\### 2.3 Repository Structure

\- Created a clear, instructor‑aligned repo structure including:

&nbsp; - `docs/` for documentation  

&nbsp; - `notebooks/` for EDA and modeling  

&nbsp; - `src/` for ingestion and model code  

&nbsp; - `reports/` for final deliverables  

&nbsp; - `environment.yml` and `.gitignore`

\- Added ingestion scripts (`data\_ingest.py`, `data\_download.py`).



\### 2.4 Instructor Feedback Responses

\- Added a polished scalability section to `system\_design.md`.

\- Added a clear, technically grounded CNN vs. LSTM justification in `CNN\_vs\_LSTM\_Justification.md`.



\### 2.5 System Design Outline

\- Drafted a complete IoT system design document covering sensors, edge processing, networking, cloud ingestion, storage, ML pipelines, and scalability.



---



\## 3. In‑Progress Items



\- Additional EDA visualizations (optional enhancements).

\- Early preprocessing refinements for Week 2 modeling tasks.

\- Planning for IoT system diagram (scheduled for Week 2).



---



\## 4. Risks and Mitigations



| Risk | Status | Mitigation |

|------|--------|------------|

| Dataset size and processing overhead | Low | Using 1‑minute resampling and a 180‑day slice keeps compute manageable. |

| Channel inconsistencies across houses | Low | Selected appliances with strong coverage and clear signatures. |

| Team coordination | Low | Weekly syncs and GitHub issue tracking in place. |



---



\## 5. Next Steps (Week 2 Preview)



\- Finalize IoT system diagram.

\- Begin CNN NILM model development.

\- Expand preprocessing pipeline for model readiness.

\- Continue refining documentation for clarity and alignment with final report.



---



\## 6. Summary



The team successfully completed all Week 1 deliverables, including dataset selection, EDA, repository setup, and required written components. The project is on schedule, and the foundation is solid for Week 2’s modeling and system design tasks.






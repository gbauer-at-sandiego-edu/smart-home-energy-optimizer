\# House Selection Decision Matrix



| Criterion | House 1 | House 2 | House 5 |

|----------|---------|---------|---------|

| Recording duration | Excellent | Very good | Moderate |

| Number of appliances | High | High | Low |

| High‑frequency data | Yes | Yes | Yes |

| Data quality | High | High | Medium |

| Missingness | Low | Low | Medium |

| Suitability for forecasting | Excellent | Good | Fair |

| Suitability for NILM | Good | Excellent | Fair |

| Recommended | Yes | Yes | No |



\## Summary of House Selection



Based on the decision matrix above, we selected House 1 and House 2 as the primary data sources for this project. Both houses offer long recording durations, high‑quality mains data, and a rich set of appliance‑level channels, which makes them strong candidates for both NILM and forecasting tasks. House 1 provides excellent continuity and low missingness, making it ideal for next‑hour forecasting, while House 2 offers highly distinctive appliance signatures that support CNN‑based NILM. In contrast, House 5 has shorter recordings, fewer appliances, and more missing data, which limits its usefulness for our modeling goals. For these reasons, Houses 1 and 2 provide the most reliable and representative foundation for our Smart Home Energy Optimizer system.



\## Data Slice Selection



To keep the project computationally manageable while still preserving meaningful temporal patterns, we selected a 180‑day slice of data and resampled all channels to a 1‑minute interval. The UK‑DALE dataset includes high‑frequency readings (1–6 seconds), but processing the full resolution across multiple houses would introduce unnecessary overhead for our modeling goals. A 1‑minute sampling rate retains the key appliance signatures needed for NILM and preserves daily and weekly patterns required for forecasting, while significantly reducing file size and training time. The 180‑day window provides enough seasonal and behavioral variation to train robust models without overwhelming storage or compute resources.



\## Channel Selection



For appliance‑level modeling, we focused on a subset of channels that are both well‑represented in the dataset and relevant for NILM. Appliances such as the kettle, refrigerator, and washing machine were selected because they appear consistently across houses, have distinctive power signatures, and contribute meaningfully to household energy usage. These appliances also span different behavioral patterns—short bursts (kettle), cyclical loads (refrigerator), and longer operational cycles (washer)—which helps the CNN learn a diverse set of activation patterns. Channels with sparse usage, inconsistent labeling, or high missingness were excluded to avoid introducing noise into the NILM model.



\## Limitations



While Houses 1 and 2 provide strong coverage for our modeling tasks, the dataset still presents several limitations. Not all appliances are sub‑metered, which means the NILM model must generalize from partial labels. Some channels contain short gaps or irregular sampling intervals that require interpolation or smoothing. Additionally, the dataset reflects the behavior of a small number of UK households, which may limit generalizability to other regions or housing types. These limitations do not prevent effective modeling, but they do shape how we interpret results and highlight the importance of careful preprocessing and validation.




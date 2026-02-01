\# CNN vs. LSTM Justification



As we started shaping the modeling strategy for this project, it became clear that we were dealing with two very different types of questions. On one hand, we wanted to identify which appliance was turning on or off at a given moment. On the other, we needed to predict how much energy the home would use in the next hour. Even though both tasks use electricity data, the underlying patterns behave differently, so it makes sense to use different deep learning architectures.



\## Why a CNN fits the NILM task



Appliance events tend to show up in the mains power signal as short, distinctive patterns. A kettle turning on produces a sharp spike, while a refrigerator cycles in a more rhythmic way. These patterns are localized in time and have recognizable shapes, which makes them a natural fit for Convolutional Neural Networks (CNNs). CNNs excel at learning local features from sliding windows of data, so they can pick up on these appliance “signatures” without needing to remember long sequences. This makes them well‑suited for Non‑Intrusive Load Monitoring (NILM), where the goal is to detect which appliance is active based on the shape of the signal.



\## Why an LSTM (or GRU) fits the forecasting task



Forecasting whole‑home energy usage is a different challenge. Instead of short bursts or localized patterns, we’re trying to capture broader temporal trends—daily routines, seasonal patterns, and gradual changes in household behavior. Long Short‑Term Memory (LSTM) and GRU models are designed for exactly this kind of sequence modeling. Their gated architecture allows them to retain information over longer periods, making them better at predicting what will happen next based on what has happened over the past several hours or days.



\## Why using both models makes sense



By pairing a CNN for NILM with an LSTM/GRU for forecasting, we’re aligning each model with the type of temporal structure it handles best. The CNN focuses on short‑duration appliance signatures, while the LSTM handles long‑range temporal dependencies. Together, they give us a more complete and interpretable picture of household energy behavior, which strengthens the overall design of our Smart Home Energy Optimizer system.


flowchart TD



&nbsp;   ROOT\["MQTT Broker<br/>(TLS + Auth)"]



&nbsp;   %% House-level root

&nbsp;   ROOT --> H1\["house/1/"]

&nbsp;   ROOT --> H2\["house/2/"]

&nbsp;   ROOT --> HN\["house/{house\_id}/"]



&nbsp;   %% Mains topics

&nbsp;   H1 --> H1\_MAINS\["house/1/mains"]

&nbsp;   H2 --> H2\_MAINS\["house/2/mains"]

&nbsp;   HN --> HN\_MAINS\["house/{house\_id}/mains"]



&nbsp;   %% Appliance topics

&nbsp;   H1 --> H1\_APP\["house/1/appliance/{appliance\_id}"]

&nbsp;   H2 --> H2\_APP\["house/2/appliance/{appliance\_id}"]

&nbsp;   HN --> HN\_APP\["house/{house\_id}/appliance/{appliance\_id}"]



&nbsp;   %% Alerts

&nbsp;   H1 --> H1\_ALERT\["house/1/alerts"]

&nbsp;   H2 --> H2\_ALERT\["house/2/alerts"]

&nbsp;   HN --> HN\_ALERT\["house/{house\_id}/alerts"]



&nbsp;   %% Metadata

&nbsp;   ROOT --> META\["system/metadata/"]

&nbsp;   META --> DEVICES\["system/metadata/devices"]

&nbsp;   META --> MODELS\["system/metadata/models"]




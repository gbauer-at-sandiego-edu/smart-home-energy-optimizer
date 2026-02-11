flowchart TB



&nbsp;   %% Device Layer

&nbsp;   subgraph DEVICE\["Device Identity \& Authentication"]

&nbsp;       CERTS\["Device Certificates<br/>X.509 / Unique Keys"]

&nbsp;       SIGN\["Message Signing<br/>Integrity Protection"]

&nbsp;   end



&nbsp;   %% Network Security

&nbsp;   subgraph NET\["Network Security"]

&nbsp;       TLS\["TLS Encryption<br/>MQTT over TLS 1.2/1.3"]

&nbsp;       AUTH\["MQTT Authentication<br/>Username/Password or Cert‑based"]

&nbsp;       ACL\["MQTT Topic ACLs<br/>house\_id scoping"]

&nbsp;   end



&nbsp;   %% Cloud IAM

&nbsp;   subgraph IAM\["Cloud IAM \& Access Control"]

&nbsp;       ROLE\_EDGE\["Edge Role<br/>Publish‑only permissions"]

&nbsp;       ROLE\_INGEST\["Ingestion Role<br/>Write to storage"]

&nbsp;       ROLE\_ML\["ML Role<br/>Read curated data<br/>Write ML outputs"]

&nbsp;       ROLE\_DASH\["Dashboard Role<br/>Read‑only access"]

&nbsp;   end



&nbsp;   %% Storage Security

&nbsp;   subgraph STORAGE\["Storage Security"]

&nbsp;       ENC\_AT\_REST\["Encryption at Rest<br/>TSDB • Object Storage"]

&nbsp;       ENC\_IN\_TRANSIT\["Encryption in Transit<br/>HTTPS / TLS"]

&nbsp;       ACCESS\_POL\["Fine‑grained Access Policies"]

&nbsp;   end



&nbsp;   %% Dashboard Security

&nbsp;   subgraph DASH\["Dashboard Security"]

&nbsp;       USER\_AUTH\["User Authentication<br/>SSO / OAuth"]

&nbsp;       ROLE\_BASED\["Role‑Based Views<br/>Admin • Analyst • Viewer"]

&nbsp;   end



&nbsp;   %% Connections

&nbsp;   CERTS --> TLS --> AUTH --> ACL

&nbsp;   AUTH --> ROLE\_EDGE

&nbsp;   ROLE\_EDGE --> ROLE\_INGEST --> STORAGE

&nbsp;   STORAGE --> ROLE\_ML --> DASH

&nbsp;   DASH --> USER\_AUTH --> ROLE\_BASED




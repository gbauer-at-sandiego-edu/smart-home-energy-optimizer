flowchart TD



&nbsp;   %% Root of the HDF5 file

&nbsp;   ROOT\["/ (RootGroup)"]



&nbsp;   %% Buildings

&nbsp;   ROOT --> B1\["/building1"]

&nbsp;   ROOT --> B2\["/building2"]

&nbsp;   ROOT --> B3\["/building3"]

&nbsp;   ROOT --> B4\["/building4"]

&nbsp;   ROOT --> B5\["/building5"]



&nbsp;   %% Elec groups

&nbsp;   B1 --> B1E\["/building1/elec"]

&nbsp;   B2 --> B2E\["/building2/elec"]

&nbsp;   B3 --> B3E\["/building3/elec"]

&nbsp;   B4 --> B4E\["/building4/elec"]

&nbsp;   B5 --> B5E\["/building5/elec"]



&nbsp;   %% Building 1 meters (abbreviated for readability)

&nbsp;   B1E --> B1M1\["meter1"]

&nbsp;   B1E --> B1M2\["meter2"]

&nbsp;   B1E --> B1M3\["meter3"]

&nbsp;   B1E --> B1M4\["meter4"]

&nbsp;   B1E --> B1M5\["meter5"]

&nbsp;   B1E --> B1M6\["meter6"]

&nbsp;   B1E --> B1M7\["meter7"]

&nbsp;   B1E --> B1M8\["meter8"]

&nbsp;   B1E --> B1M9\["meter9"]

&nbsp;   B1E --> B1M10\["meter10"]

&nbsp;   B1E --> B1M11\["meter11"]

&nbsp;   B1E --> B1M12\["meter12"]

&nbsp;   B1E --> B1M13\["meter13"]

&nbsp;   B1E --> B1M14\["meter14"]

&nbsp;   B1E --> B1M15\["meter15"]

&nbsp;   B1E --> B1M16\["meter16"]

&nbsp;   B1E --> B1M17\["meter17"]

&nbsp;   B1E --> B1M18\["meter18"]

&nbsp;   B1E --> B1M19\["meter19"]

&nbsp;   B1E --> B1M20\["meter20"]

&nbsp;   B1E --> B1M21\["meter21"]

&nbsp;   B1E --> B1M22\["meter22"]

&nbsp;   B1E --> B1M23\["meter23"]

&nbsp;   B1E --> B1M24\["meter24"]

&nbsp;   B1E --> B1M25\["meter25"]

&nbsp;   B1E --> B1M26\["meter26"]

&nbsp;   B1E --> B1M27\["meter27"]

&nbsp;   B1E --> B1M28\["meter28"]

&nbsp;   B1E --> B1M29\["meter29"]

&nbsp;   B1E --> B1M30\["meter30"]

&nbsp;   B1E --> B1M31\["meter31"]

&nbsp;   B1E --> B1M32\["meter32"]

&nbsp;   B1E --> B1M33\["meter33"]

&nbsp;   B1E --> B1M34\["meter34"]

&nbsp;   B1E --> B1M35\["meter35"]

&nbsp;   B1E --> B1M36\["meter36"]

&nbsp;   B1E --> B1M37\["meter37"]

&nbsp;   B1E --> B1M38\["meter38"]

&nbsp;   B1E --> B1M39\["meter39"]

&nbsp;   B1E --> B1M40\["meter40"]

&nbsp;   B1E --> B1M41\["meter41"]

&nbsp;   B1E --> B1M42\["meter42"]

&nbsp;   B1E --> B1M43\["meter43"]

&nbsp;   B1E --> B1M44\["meter44"]

&nbsp;   B1E --> B1M45\["meter45"]

&nbsp;   B1E --> B1M46\["meter46"]

&nbsp;   B1E --> B1M47\["meter47"]

&nbsp;   B1E --> B1M48\["meter48"]

&nbsp;   B1E --> B1M49\["meter49"]

&nbsp;   B1E --> B1M50\["meter50"]

&nbsp;   B1E --> B1M51\["meter51"]

&nbsp;   B1E --> B1M52\["meter52"]

&nbsp;   B1E --> B1M53\["meter53"]

&nbsp;   B1E --> B1M54\["meter54"]



&nbsp;   %% Each meter contains a table node

&nbsp;   B1M1 --> B1M1T\["table"]

&nbsp;   B1M2 --> B1M2T\["table"]

&nbsp;   B1M3 --> B1M3T\["table"]

&nbsp;   %% (You can expand more if needed)



&nbsp;   %% Building 2 meters (abbreviated)

&nbsp;   B2E --> B2M1\["meter1"]

&nbsp;   B2E --> B2M2\["meter2"]

&nbsp;   B2E --> B2M3\["meter3"]

&nbsp;   B2E --> B2M4\["meter4"]

&nbsp;   B2E --> B2M5\["meter5"]

&nbsp;   B2E --> B2M6\["meter6"]

&nbsp;   B2E --> B2M7\["meter7"]

&nbsp;   B2E --> B2M8\["meter8"]

&nbsp;   B2E --> B2M9\["meter9"]

&nbsp;   B2E --> B2M10\["meter10"]

&nbsp;   B2E --> B2M11\["meter11"]

&nbsp;   B2E --> B2M12\["meter12"]

&nbsp;   B2E --> B2M13\["meter13"]

&nbsp;   B2E --> B2M14\["meter14"]

&nbsp;   B2E --> B2M15\["meter15"]

&nbsp;   B2E --> B2M16\["meter16"]

&nbsp;   B2E --> B2M17\["meter17"]

&nbsp;   B2E --> B2M18\["meter18"]

&nbsp;   B2E --> B2M19\["meter19"]

&nbsp;   B2E --> B2M20\["meter20"]



&nbsp;   %% Building 3 meters

&nbsp;   B3E --> B3M1\["meter1"]

&nbsp;   B3E --> B3M2\["meter2"]

&nbsp;   B3E --> B3M3\["meter3"]

&nbsp;   B3E --> B3M4\["meter4"]

&nbsp;   B3E --> B3M5\["meter5"]



&nbsp;   %% Building 4 meters

&nbsp;   B4E --> B4M1\["meter1"]

&nbsp;   B4E --> B4M2\["meter2"]

&nbsp;   B4E --> B4M3\["meter3"]

&nbsp;   B4E --> B4M4\["meter4"]

&nbsp;   B4E --> B4M5\["meter5"]

&nbsp;   B4E --> B4M6\["meter6"]



&nbsp;   %% Building 5 meters (abbreviated)

&nbsp;   B5E --> B5M1\["meter1"]

&nbsp;   B5E --> B5M2\["meter2"]

&nbsp;   B5E --> B5M3\["meter3"]

&nbsp;   B5E --> B5M4\["meter4"]

&nbsp;   B5E --> B5M5\["meter5"]

&nbsp;   B5E --> B5M6\["meter6"]

&nbsp;   B5E --> B5M7\["meter7"]

&nbsp;   B5E --> B5M8\["meter8"]

&nbsp;   B5E --> B5M9\["meter9"]

&nbsp;   B5E --> B5M10\["meter10"]

&nbsp;   B5E --> B5M11\["meter11"]

&nbsp;   B5E --> B5M12\["meter12"]

&nbsp;   B5E --> B5M13\["meter13"]

&nbsp;   B5E --> B5M14\["meter14"]

&nbsp;   B5E --> B5M15\["meter15"]

&nbsp;   B5E --> B5M16\["meter16"]

&nbsp;   B5E --> B5M17\["meter17"]

&nbsp;   B5E --> B5M18\["meter18"]

&nbsp;   B5E --> B5M19\["meter19"]

&nbsp;   B5E --> B5M20\["meter20"]

&nbsp;   B5E --> B5M21\["meter21"]

&nbsp;   B5E --> B5M22\["meter22"]

&nbsp;   B5E --> B5M23\["meter23"]

&nbsp;   B5E --> B5M24\["meter24"]

&nbsp;   B5E --> B5M25\["meter25"]

&nbsp;   B5E --> B5M26\["meter26"]




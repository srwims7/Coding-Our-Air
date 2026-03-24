# Coding Our Air — Philadelphia County Air Emissions

A data visualization project mapping greenhouse gas emissions from facilities in Philadelphia County, PA.

---

## Files

| File | Description |
|------|-------------|
| `carbondioxide.csv` | Original 2019 PA DEP emissions data (139 facilities, CO₂ only) |
| `Eng WINS Carbon Dioxide Emissions in 2019 from Philadelphia County.ipynb` | Original Jupyter notebook — static 2019 CO₂ map using folium |
| `Philadelphia_Air_Emissions_Map.html` | **Updated interactive map** — open directly in any browser, no server needed |
| `README.md` | This file |

---

## How to Use the Interactive Map

1. Download or clone this repo
2. Open `Philadelphia_Air_Emissions_Map.html` in any web browser (double-click it)
3. Use the **Year & Pollutants** panel (top right) to:
   - Select a year from **2010 to 2023**
   - Check/uncheck pollutants: Carbon Dioxide, Methane, Nitrous Oxide, Biogenic CO₂
4. Click any circle on the map to see the facility name and emission amount
5. Use the **Emission Rank** legend (bottom left) to interpret colors — collapse it when you want a cleaner view

---

## Data Sources

- **2010–2019:** Pennsylvania Department of Environmental Protection (PA DEP) Air Information Management System (AIMS)
- **2020–2023:** Estimated from EPA Greenhouse Gas Reporting Program (GHGRP) trends
  - 2020 data reflects the closure of the Philadelphia Energy Solutions refinery (June 2019 fire) and COVID-19 impacts

---

## Color Key

Colors are assigned by **emission rank** within the selected year — not by fixed thresholds — so the highest emitter is always darkred regardless of the year.

| Color | Rank |
|-------|------|
| 🔴 Dark Red | Highest emitters |
| 🔴 Red | Very high |
| 🟠 Orange | High |
| 🩷 Pink | Moderate |
| 🟤 Beige | Low-moderate |
| ⚫ Gray | Low |
| ⚪ Light Gray | Very low |
| ⚫ Black | Lowest emitters |

---

## Original Project

The original notebook was created as part of the **Eng WINS** program at Drexel University (2021), focusing on CO₂ emissions in Philadelphia County for 2019.

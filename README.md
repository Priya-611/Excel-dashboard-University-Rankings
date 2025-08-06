# University Rankings Dashboard (2016-2025)

## Project Overview
This project presents an analytical view of the **Times Higher Education (THE) World University Rankings**, using data from 2016–2025. It involves cleaning the raw dataset with Python and developing an insightful **Excel Dashboard** to analyze global university performance across various dimensions like teaching, research, gender diversity, and international presence.


---


## Dataset Source
- **Website:** [THE World University Rankings 2024](https://www.timeshighereducation.com/world-university-rankings/2024/world-ranking)
- **Raw Dataset:** `THE World University Rankings 2016-2025.csv`
- **Cleaned Dataset:** `Cleaned_University_Ranking.xlsx`


---


## Project Workflow
1. **Data Collection:** Extracted the dataset from the official source.
2. **Data Cleaning with Python (`uni_ranking.py`):**
   - Extracted numerical values from text-based columns (e.g., Female:Male Ratio).
   - Handled missing values using group-wise and overall averages.
   - Standardized percentage values into decimal format.
   - Created new features like `Female`, `Male` percentages.
3. **Data Export:** Saved the cleaned data into Excel format.
4. **Excel Dashboard Creation:**
   - Built a user-friendly dashboard with charts, pivot tables, and slicers.
   - Enabled filters for country, year, and metrics.


---


## Analytical Objectives
- **Top 10 Countries by Student Population**
- **Top 5 Universities with Highest Overall Score**
- **Top 10 Universities with Highest Teaching Score (2024 & 2025)**
- **Top 5 Universities with Best Average Student to Staff Ratio**
- **Top 5 Universities with Highest Average International Outlook**
- **Comparison of Average Male & Female % in US vs UK**
- **Top 5 Countries with Highest Yearly Average Female %**
- **Top 10 Universities with Highest Average Industry Impact**
- **Correlation between Research Quality and Overall Score**


---


## Features of the Dashboard
- Dynamic year-wise comparison and ranking filters.
- Bar, line, and pie charts for visual interpretation.
- Gender diversity breakdown.
- Teaching, research, and international outlook analysis.
- Quick insights through pivot summaries and conditional formatting.


---


## Tools Used
- **Python**: Data wrangling with Pandas and NumPy.
- **Excel**: Data visualization and dashboard creation using Pivot Charts, Slicers, and Filters.
- **Libraries Used**: `pandas`, `numpy`, `matplotlib`, `seaborn` (for optional EDA).


---


## File Structure
university-rankings-dashboard/

├── THE World University Rankings 2016-2025.csv `Raw dataset`

├── uni_ranking.py `Python script for data cleaning`

├── Cleaned_University_Ranking.xlsx `Cleaned and processed dataset`

├── University_Rankings_Dashboard.xlsx `Final Excel dashboard`

└── README.md `Project documentation`




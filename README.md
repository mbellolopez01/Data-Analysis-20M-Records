# Data Analysis & Demographic Profiling (20M+ Records)

## 📌 Project Overview
This project focuses on the end-to-end processing, cleaning, and visualization of a massive dataset containing over **20.4 million records**. The primary goal was to transform fragmented raw data from multiple sources into a high-performance interactive Dashboard for population segmentation and contactability analysis.

## 🛠️ Tech Stack
* **Python (Pandas & PyArrow):** Used for the ETL process, consolidating 24+ Excel files and converting them into **Apache Parquet** format to optimize memory usage and processing speed.
* **Power BI / Power Query:** Data modeling and interactive dashboard design.
* **DAX (Data Analysis Expressions):** Created custom measures for dynamic contactability and demographic KPIs.
* **Apache Parquet:** Implemented as the core storage format, reducing dataset size by over 70% and enabling fluid performance on standard hardware.

## 📊 Key Insights & Visualizations
The final Dashboard provides real-time insights into:
* **Contactability:** High-level overview of verified phone numbers (72% coverage) and email reach.
* **Demographics:** Population distribution by Age Groups (10-year bins), Gender, and Location.
* **Geographic Granularity:** Drill-down capabilities from State level down to specific Municipalities and Parishes.

## 🚀 Technical Challenges & Solutions
* **Memory Management:** Solved RAM overflow issues when handling large Excel files by implementing a Python-based ETL pipeline.
* **Performance Optimization:** Migrated from standard CSV/Excel connections to a single-source Parquet environment, resulting in a 300% faster data refresh rate in Power BI.
* **Data Integrity:** Standardized inconsistent fields across 20 million rows, specifically ensuring correct formatting for identification numbers and contact details.

## 📈 Results
* Successfully mapped the demographic profile of 20.4M individuals.
* Identified the 30-40 age group as the most prominent demographic segment.
* Built a scalable system capable of filtering millions of rows instantly.

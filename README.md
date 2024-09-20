# Beijing Air Quality Analysis Project

## Dashboard URL
()

---

## Overview

This project focuses on analyzing  and developing an interactive dashboard for analyzing air quality in Beijing using hourly air pollutant data from 12 nationally-controlled air-quality monitoring stations. The air-quality data, collected by the **Beijing Municipal Environmental Monitoring Center**, includes pollutants such as PM2.5, PM10, SO2, NO2, CO, and O3. The analysis are specified for PM2.5 and PM10 pollutant level and understanding the relations with various period and environment. The dashboard allows users to explore trends in air quality over time, compare pollutant levels across various locations, and analyze the effect of meteorological factors such as wind direction on pollutant concentration.

---

## Dataset Description

The dataset used in this project is provided by the **Beijing Municipal Environmental Monitoring Center**. It includes hourly measurements of six key air pollutants from 12 monitoring sites located across Beijing. The data covers a wide time frame and includes the following variables:

- **PM2.5**: Particulate matter with a diameter of 2.5 micrometers or less.
- **PM10**: Particulate matter with a diameter of 10 micrometers or less.
- **SO2**: Sulfur dioxide, a gas primarily produced by industrial activities.
- **NO2**: Nitrogen dioxide, largely from vehicle emissions and industrial combustion.
- **CO**: Carbon monoxide, a colorless, odorless gas produced from incomplete combustion.
- **O3**: Ozone, formed by chemical reactions between pollutants in sunlight.
- **Datetime**: Timestamps indicating the time of the measurements.
- **Wind Direction (wd)**: Wind direction recorded during the measurement to study its influence on pollutant levels.

---

## Key Insights

Key insights gained from this dashboard include:
- **Seasonal Trends**: Pollutant levels, particularly PM2.5 and PM10, show distinct seasonal trends with peaks during winter months.
- **Daily Patterns**: Pollutant concentrations typically vary throughout the day, with higher levels observed during peak traffic hours at night.
- **Correlation With Weathers**: Some variable that describe weather condition such as rainfall, wind speed, and temperature have negative correlation with pollutant level, while dew points have positive correlation with pollutant level.
- **Wind Direction Impact**: Wind direction plays a significant role in pollutant dispersion. Certain pollutants are more prevalent under specific wind conditions.

---

## **Installation Guide**

### **Requirements**
Ensure you have the following software and libraries installed:
- **Python 3.7+**
- **Streamlit**: Used to create the dashboard interface.
- **Pandas**: For data manipulation.
- **Matplotlib & Seaborn**: For generating visualizations.
- **NumPy**: For numerical computations.
- **Plotly**: For interactive graphs.

### Installation Steps
1. **Clone the Repository**  
   Download the project files by cloning the repository:
   ```bash
   git clone https://github.com/your-username/air-quality-analysis.git
   cd air-quality-analysis
   ```

2. **Set Up a Virtual Environment (optional but recommended)**  
   It’s recommended to create a virtual environment to manage dependencies. You can choose between venv or conda:
   - For venv:
    ```bash
    python3 -m venv env
    source env/bin/activate  # For Linux/macOS
    env\Scripts\activate  # For Windows
    ```
    - For Conda (ensure [Conda](https://docs.conda.io/en/latest/) is installed):
    ```bash
    conda create --name airquality-env
    conda activate airquality-env
    ```

3. **Install Required Libraries**  
   Install the necessary Python libraries using `requirements.txt`:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Streamlit Dashboard**  
   Launch the dashboard using Streamlit:
   ```bash
   streamlit run app.py
   ```

5. **Explore the Dashboard**  
   Open your browser and navigate to the URL displayed in your terminal (usually `http://localhost:8501`).

---

# About Me
- **Name**: Farras Rafi' Permana
- **Email**: farras2003@gmail.com
- **Dicoding ID**: [farrasrafi](https://www.dicoding.com/users/farrasrafi/)

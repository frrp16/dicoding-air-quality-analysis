import streamlit as st
import numpy as np
import warnings
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from scipy import stats

warnings.filterwarnings('ignore')

st.set_page_config(page_title="Beijing Air Quality Analysis")

merged_df = pd.read_csv("dataset/air-quality-dataset-merged.csv")
merged_df['datetime'] = pd.to_datetime(merged_df['datetime'])


st.title("Air Quality Data Dashboard")

st.markdown("""
This dashboard provides a detailed analysis of air quality data collected from 12 nationally-controlled air-quality monitoring stations in Beijing. The data includes hourly measurements of major air pollutants such as PM2.5, PM10, SO2, NO2, CO, and O3. Through interactive visualizations, users can explore how pollutant levels fluctuate over time, across different stations, and under varying environmental conditions like wind direction.

Key features of the dashboard include:
- **Time Series Analysis**: View pollutant concentrations over time with options to resample data by hours, days, or months.
- **Pollutant Comparison**: Compare different pollutants side-by-side to understand how their levels correlate.
- **Wind Direction Analysis**: Analyze the effect of wind direction on pollutant concentrations using polar plots.
- **Customizable Visualizations**: Users can select specific pollutants, stations, and time ranges to explore trends in air quality.

### **Dataset Description:**

The dataset consists of hourly air pollutant measurements recorded by the **Beijing Municipal Environmental Monitoring Center**. The monitoring sites are spread across 12 nationally-controlled locations in Beijing, ensuring comprehensive coverage of the city's air quality. The dataset includes the following pollutants:
- **PM2.5**: Fine particulate matter with a diameter of 2.5 microns or less.
- **PM10**: Particulate matter with a diameter of 10 microns or less.
- **SO2**: Sulfur dioxide, a harmful gas produced by industrial processes.
- **NO2**: Nitrogen dioxide, a pollutant from vehicle emissions and combustion.
- **CO**: Carbon monoxide, a colorless, odorless gas from burning fossil fuels.
- **O3**: Ozone, a pollutant formed by reactions of pollutants under sunlight.

The dataset also includes:
- **Datetime**: Timestamp for each hourly measurement.
- **Wind Direction (wd)**: Wind direction data to analyze its effect on pollutant levels.

 """)

st.sidebar.header("Filter Options")


years = sorted(merged_df['year'].unique())
selected_year = st.sidebar.selectbox('Select Year', years)


stations = merged_df['station'].unique()
selected_station = st.sidebar.selectbox('Select Station', stations)


filtered_data = merged_df[(merged_df['year'] == selected_year) & 
                          (merged_df['station'] == selected_station)]


st.subheader(f"PM2.5 and PM10 Levels Over Time at {selected_station} in {selected_year}")

col1, col2 = st.columns(2)
with col1:
    resample_option = st.selectbox("Resample Data By", ('Hourly', 'Daily', 'Weekly','Monthly'))
with col2:
    selected_pol = st.multiselect('Select Pollutant to Display', ['PM2.5', 'PM10', 'SO2', 'NO2', 'CO', 'O3'], key=11, default=['PM2.5', 'PM10'])

if resample_option == 'Hourly':
    resampled_data = filtered_data.set_index('datetime').resample('H')[selected_pol].mean()
elif resample_option == 'Daily':
    resampled_data = filtered_data.set_index('datetime').resample('D')[selected_pol].mean()
elif resample_option == 'Weekly':
    resampled_data = filtered_data.set_index('datetime').resample('W')[selected_pol].mean()
else:  
    resampled_data = filtered_data.set_index('datetime').resample('M')[selected_pol].mean()

fig, ax = plt.subplots(figsize=(10, 6))
sns.lineplot(data=resampled_data, dashes=False, ax=ax, palette='magma', alpha=0.8)

ax.set_xlabel('Datetime')
ax.set_ylabel('Concentration')
ax.set_title(f"Pollutant Levels Over Time ({resample_option} Data)")
ax.grid(True)
st.pyplot(fig)


st.subheader("Correlation Matrix of Air Quality Features")
selected_columns = st.multiselect('Select Columns for Correlation', ['PM2.5', 'PM10', 'SO2', 'NO2', 'CO', 'O3', 'TEMP', 'PRES', 'DEWP', 'RAIN', 'WSPM'], key=22, default=['PM2.5', 'NO2', 'TEMP', 'PRES', 'DEWP'])
if selected_columns:
    corr_matrix = merged_df[selected_columns].corr()

    fig, ax = plt.subplots(figsize=(10, 8))
    sns.heatmap(corr_matrix, annot=True, fmt=".2f", cmap='coolwarm', ax=ax)
    st.pyplot(fig)
else:
    st.text("Select columns to view correlation")

st.subheader(f"Pollutant Levels Throughout the Hours of Day at {selected_station} Station")
selected_col = st.multiselect('Select Pollutant to Display', ['PM2.5', 'PM10', 'SO2', 'NO2', 'CO', 'O3'], default=['PM2.5', 'PM10'])
hourly_data = filtered_data.groupby(filtered_data['datetime'].dt.hour)[selected_col].mean()

fig, ax = plt.subplots(figsize=(10, 6))
sns.lineplot(data=hourly_data, palette='magma', markers=True, dashes=False, ax=ax)

ax.set_xlabel('Hour of the Day')
ax.set_ylabel('Concentration')
ax.set_title(f"Pollutant Levels Throughout the Day at {selected_station}")
ax.grid(True)

st.pyplot(fig)




st.subheader(f"Pollutant Levels Throughout the Days of Week at {selected_station} Station")
selected_col = st.multiselect('Select Pollutant to Display', ['PM2.5', 'PM10', 'SO2', 'NO2', 'CO', 'O3'], default=['PM2.5', 'PM10'], key=333)
hourly_data = filtered_data.groupby(filtered_data['datetime'].dt.hour)[selected_col].mean()

fig, ax = plt.subplots(figsize=(10, 6))
sns.lineplot(data=hourly_data, palette='magma', markers=True, dashes=False, ax=ax)

ax.set_xlabel('Hour of the Day')
ax.set_ylabel('Concentration')
ax.set_title(f"Pollutant Levels Throughout the Day at {selected_station}")
ax.grid(True)

st.pyplot(fig)



st.subheader(f"Average Pollutant Levels by Day of the Week at {selected_station}")

selected_pol = st.multiselect(
    'Select Pollutant to Display', 
    ['PM2.5', 'PM10', 'SO2', 'NO2', 'CO', 'O3'], 
    default=['PM2.5', 'PM10'], key=444
)

filtered_data['day_of_week'] = filtered_data['datetime'].dt.day_name()

days_order = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

pollutant_by_day = filtered_data.groupby('day_of_week')[selected_pol].mean()
pollutant_by_day = pollutant_by_day.reset_index()
pollutant_by_day['day_of_week'] = pd.Categorical(pollutant_by_day['day_of_week'], categories=days_order, ordered=True)
pollutant_by_day = pollutant_by_day.sort_values('day_of_week')

fig, ax = plt.subplots(figsize=(10, 6))

pollutant_by_day[selected_pol + ['day_of_week']].plot(x='day_of_week',kind='bar', width=0.6, ax=ax, alpha=0.8)
ax.set_xlabel('Day of the Week')
ax.set_ylabel('Average Concentration')
ax.set_title(f'Average Pollutant Levels by Day of the Week at {selected_station} station')
ax.legend(title='Pollutants')
ax.grid(True)
ax.set_xticklabels(ax.get_xticklabels(), rotation=45)
st.pyplot(fig)


st.subheader('Wind Direction Analysis')
selected_pollutant = st.selectbox(
    'Select Pollutant for Wind Direction Analysis',
    ['PM2.5', 'PM10', 'SO2', 'NO2', 'CO', 'O3'],
    index=0 
)

wind_data = filtered_data.groupby('wd')[selected_pollutant].mean()
fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(111, polar=True)
theta = np.linspace(0, 2 * np.pi, len(wind_data))
bars = ax.bar(theta, wind_data.values, align='center', alpha=0.6)
plt.title(f'{selected_pollutant} Levels by Wind Direction')
st.pyplot(fig)



st.markdown("""
### About Me:
- **Name**: Farras Rafi' Permana
- **Email**: farras2003@gmail.com
- **Dicoding ID**: [farrasrafi](https://www.dicoding.com/users/farrasrafi/)
""")
# API-INTEGRATION-AND-DATA-VISUALIZATION

*COMPANY*:CODTECH IT SOLUTIONS

*Name* :Trivedi Parth Yogeshbhai

*Intern ID* :CT04DN939

*Domain*:Python Programming

*Duration*:4 Weeks

*Mentor*:Neela Santhosh Kumar



# Weather Forecast Visualization Project

## 🌦️ Project Overview

This project is a simple yet powerful weather forecast visualizer built using Python. The goal of this project is to fetch 5-day weather forecast data for multiple cities and visualize important weather metrics like temperature and humidity in the form of clean, easy-to-read line plots. The data is pulled from the **OpenWeatherMap API**, and the plots are generated using **Matplotlib** and **Seaborn** for enhanced visuals.

The entire script is written in Python and focuses on automating the process of retrieving and displaying weather data for a list of cities. For this version, I’ve chosen three major cities in India: **Ahmedabad, Mumbai, and Delhi**. However, the project is designed to be easily scalable to include more cities or change the existing ones by simply editing a list.

This project was developed during my internship as a demonstration of my ability to integrate APIs, perform data parsing, and generate meaningful data visualizations using Python. It also shows my capability to handle real-world data and represent it in a way that is both informative and user-friendly.


## 🚀 Key Features

* **Fetch Real-Time Weather Forecasts:**
  The script uses the OpenWeatherMap API to get forecast data for the next five days, at 3-hour intervals.

* **Multiple City Support:**
  You can customize the `CITIES` list to include any cities supported by OpenWeatherMap.

* **Data Processing:**
  For each data point, the script extracts temperature, minimum and maximum temperature, humidity, and weather condition description.

* **Beautiful Visualizations:**
  The data is visualized using line graphs that compare temperature and humidity changes over time. Seaborn is used to make the plots look cleaner and more readable.

* **Datetime Handling:**
  Uses Python's `datetime` module to parse and format timestamps for plotting and display.


## 📦 Tech Stack

* **Programming Language:** Python 3
* **API:** OpenWeatherMap ([https://openweathermap.org/](https://openweathermap.org/))
* **Libraries Used:**

  * `requests` – for making HTTP requests to fetch weather data
  * `datetime` – for handling and formatting date and time
  * `matplotlib` – for plotting graphs
  * `seaborn` – for improved visual aesthetics
  * `matplotlib.dates` – for formatting x-axis time labels


## 🧠 How It Works

1. **Configuration Section:**
   At the top of the script, you can define your API key and list of cities. You can also change the unit system (default is metric).

2. **Fetch Function:**
   The `get_weather_data()` function builds the API request URL, sends it, and parses the JSON response. It returns a list of forecast entries for each city.

3. **Data Visualization:**
   The `draw_graph()` function receives the parsed forecast data and creates a two-part plot:

   * The top plot shows temperature trends: average, minimum, and maximum.
   * The bottom plot shows humidity percentages.
     Both plots use timestamps on the x-axis and appropriate metric units on the y-axis.

4. **Execution Loop:**
   A `for` loop iterates over each city in the list, fetching and plotting the weather data one by one. Each step prints progress messages in the terminal.


## ✅ How to Run the Project

1. Clone this repository or copy the code into your local Python environment.

2. Make sure you have Python 3 installed.

3. Install the required libraries:

   ```bash
   pip install requests matplotlib seaborn
   ```

4. Sign up at [OpenWeatherMap](https://openweathermap.org/) and generate your free API key.

5. Replace the `API_KEY` variable in the script with your personal key.

6. Run the script:

   ```bash
   python weather_forecast.py
   ```

7. Graphs will pop up showing forecasted temperatures and humidity levels for each city.


## 📝 Future Improvements

* Add wind speed and pressure to visualizations.
* Export plots to PNG or PDF files.
* Add a GUI or web interface using Tkinter, Flask, or Streamlit.
* Add error handling for invalid city names or network errors.


## 🙋‍♂️ Why I Made This

This project helped me understand how APIs work, how to process structured JSON data, and how to build data visualizations from real-world sources. It was also part of my internship assignment where I was asked to create a tool that uses external APIs and represents data visually. I chose weather forecasting because it's something we all interact with daily, and visualizing it helps make sense of changing climate conditions.

*output*
![Image](https://github.com/user-attachments/assets/9413e6e3-8af5-4f1d-a95a-d60ecbe84cac)



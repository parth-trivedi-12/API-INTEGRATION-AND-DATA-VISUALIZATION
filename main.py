import requests
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime
import matplotlib.dates as mdates

# Configuration
API_KEY = "04f701d763a96b997fa319be23fb6343"
CITIES = ["Ahmedabad", "Mumbai", "Delhi"]
UNITS = "metric"

# Get forecast data from API
def get_weather_data(city, key):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={key}&units={UNITS}"
    res = requests.get(url)
    info = res.json()

    if "list" not in info:
        print(f"Failed to get data for {city} - {info.get('message', 'No info')}")
        return []

    records = []
    for i in info["list"]:
        records.append({
            "datetime": datetime.strptime(i["dt_txt"], "%Y-%m-%d %H:%M:%S"),
            "temp": i["main"]["temp"],
            "temp_min": i["main"]["temp_min"],
            "temp_max": i["main"]["temp_max"],
            "humidity": i["main"]["humidity"],
            "weather": i["weather"][0]["description"].capitalize()
        })

    return records

# Graph for temperature and humidity
def draw_graph(city, records):
    if not records:
        return

    times = [r["datetime"] for r in records]
    temps = [r["temp"] for r in records]
    t_min = [r["temp_min"] for r in records]
    t_max = [r["temp_max"] for r in records]
    humid = [r["humidity"] for r in records]

    sns.set(style="whitegrid")
    fig, ax = plt.subplots(2, 1, figsize=(13, 9), sharex=True)

    # Plot temperature
    ax[0].plot(times, temps, label="Temp °C", color="blue", marker='.')
    ax[0].plot(times, t_min, label="Min", linestyle='--', color="orange")
    ax[0].plot(times, t_max, label="Max", linestyle='--', color="green")
    ax[0].set_title(f"{city} - Temp Forecast")
    ax[0].set_ylabel("°C")
    ax[0].legend()

    # Plot humidity
    ax[1].plot(times, humid, label="Humidity %", color="purple", marker='x')
    ax[1].set_title(f"{city} - Humidity Forecast")
    ax[1].set_ylabel("%")
    ax[1].legend()

    ax[1].set_xlabel("Date/Time")
    ax[1].xaxis.set_major_formatter(mdates.DateFormatter('%m-%d %H:%M'))
    plt.xticks(rotation=40)

    plt.tight_layout()
    plt.show()

# Run for each city
for c in CITIES:
    print(f"Getting weather info for {c}...")
    weather_data = get_weather_data(c, API_KEY)
    draw_graph(c, weather_data)
    print(f"Done with {c}\n")

import requests
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime
import matplotlib.dates as mdates

# === CONFIG ===
API_KEY = "04f701d763a96b997fa319be23fb6343"
CITIES = ["Ahmedabad", "Mumbai", "Delhi"]
UNITS = "metric"

# === Fetch and Parse Weather Data ===
def fetch_weather_data(city, api_key):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={api_key}&units={UNITS}"
    response = requests.get(url)
    data = response.json()

    if "list" not in data:
        print(f"❌ Failed to fetch fo
        r {city}: {data.get('message', 'Unknown error')}")
        return []

    forecast_list = []
    for entry in data["list"]:
        forecast_list.append({
            "datetime": datetime.strptime(entry["dt_txt"], "%Y-%m-%d %H:%M:%S"),
            "temp": entry["main"]["temp"],
            "temp_min": entry["main"]["temp_min"],
            "temp_max": entry["main"]["temp_max"],
            "humidity": entry["main"]["humidity"],
            "weather": entry["weather"][0]["description"].capitalize()
        })

    return forecast_list

# === Plot Forecast ===
def plot_forecast(city, data):
    if not data:
        return

    dates = [entry["datetime"] for entry in data]
    temps = [entry["temp"] for entry in data]
    min_temps = [entry["temp_min"] for entry in data]
    max_temps = [entry["temp_max"] for entry in data]
    humidity = [entry["humidity"] for entry in data]
    weather = [entry["weather"] for entry in data]

    sns.set(style="darkgrid")
    fig, axs = plt.subplots(2, 1, figsize=(14, 10), sharex=True)

    # === Temperature Plot ===
    axs[0].plot(dates, temps, label="Temperature (°C)", color="royalblue", marker='o')
    axs[0].plot(dates, min_temps, label="Min Temp", linestyle='--', color="tomato")
    axs[0].plot(dates, max_temps, label="Max Temp", linestyle='--', color="green")
    axs[0].set_title(f"Temperature Forecast - {city}")
    axs[0].set_ylabel("Temperature (°C)")
    axs[0].legend()

    # === Humidity Plot ===
    axs[1].plot(dates, humidity, label="Humidity (%)", color="purple", marker='s')
    axs[1].set_title(f"Humidity Forecast - {city}")
    axs[1].set_ylabel("Humidity (%)")
    axs[1].legend()

    # === Shared Settings ===
    axs[1].set_xlabel("Date & Time")
    plt.xticks(rotation=45)
    axs[1].xaxis.set_major_formatter(mdates.DateFormatter('%m-%d %H:%M'))

    plt.tight_layout()
    plt.show()

# === Main Execution ===
for city in CITIES:
    print(f"📡 Fetching data for {city}...")
    city_data = fetch_weather_data(city, API_KEY)
    plot_forecast(city, city_data)
    print(f"✅ Finished plotting for {city}\n")



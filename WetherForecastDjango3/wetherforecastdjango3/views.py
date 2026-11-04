from django.http import HttpResponse
from django.shortcuts import render
import requests


def main_page(request):
  return render(request, "main.html")


def second_page(request):
  name = request.GET.get("name", "Олександр")
  context = {"name": name}
  return render(request, "second.html", context)


def weather_odesa(request):
  lat = 46.48
  lon = 30.73

  url = "https://api.open-meteo.com/v1/forecast"
  params = {
      "latitude": lat,
      "longitude": lon,
      "current": (
          "temperature_2m,relative_humidity_2m,wind_speed_10m,weather_code"
      ),
      "timezone": "Europe/Kyiv",
      "forecast_days": 1,
  }

  context = {}

  try:
    r = requests.get(url, params=params, timeout=8)
    r.raise_for_status()
    data = r.json()

    current = data["current"]
    weather_code = current.get("weather_code", 0)
    conditions = {
        0: "Ясно",
        1: "Мало хмар",
        2: "Розсіяні хмари",
        3: "Похмуро",
        45: "Туман",
        51: "Легкий дощ",
        61: "Дощ",
    }.get(weather_code, "Невідомо")

    context = {
        "temp": current["temperature_2m"],
        "humidity": current["relative_humidity_2m"],
        "wind": current["wind_speed_10m"],
        "conditions": conditions,
        "time_update": current["time"],
    }

  except requests.RequestException as e:
    context = {"error": str(e)}

  return render(request, "weather.html", context)
import random
from typing import Protocol, runtime_checkable
import httpx


@runtime_checkable
class TemperatureSensor(Protocol):
  """Протокол (контракт) для датчиків температури"""

  def read_temperature(self) -> float:
    ...

  def get_sensor_id(self) -> str:
    ...

class WeatherAPISensor:

  def get_sensor_id(self) -> str:
    return "Odesa"

  def read_temperature(self) -> float:
    try:
      response = httpx.get(
          "https://api.open-meteo.com/v1/forecast",
          params={
              "latitude": 46.477,
              "longitude": 30.733,
              "current_weather": "true",
          },
          timeout=5.0,
      )
      response.raise_for_status()
      data = response.json()["current_weather"]
      return float(data["temperature"])
    except Exception as e:
      raise ConnectionError(f"Не вдалося отримати дані з API: {e}")

class SimulatedSensor:

  def __init__(self, base: float, deviation: float):
    self.base = base
    self.deviation = deviation

  def get_sensor_id(self) -> str:
    return "Simulated-Sensor-01"

  def read_temperature(self) -> float:
    offset = random.uniform(-self.deviation, self.deviation)
    return round(self.base + offset, 2)

class FakeAlways25:

  def get_sensor_id(self) -> str:
    return "Fake-25"

  def read_temperature(self) -> float:
    return 25.0

class StaticOfficeSensor:

  def get_sensor_id(self) -> str:
    return "Office-Sensor-Bulgaria"

  def read_temperature(self) -> float:
    return 21.5
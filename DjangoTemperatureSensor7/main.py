from sensors import (
    FakeAlways25,
    SimulatedSensor,
    StaticOfficeSensor,
    TemperatureSensor,
    WeatherAPISensor,
)

if __name__ == "__main__":
  sensors = [
      WeatherAPISensor(),
      SimulatedSensor(base=20.0, deviation=3.5),
      FakeAlways25(),
      StaticOfficeSensor(),
  ]

  print("тестування датчикив темпаратури\n")

  for sensor in sensors:
    is_valid = isinstance(sensor, TemperatureSensor)

    sensor_id = sensor.get_sensor_id()
    try:
      temp = sensor.read_temperature()
      print(
          f"ID: {sensor_id} Температура: {temp} °C"
          f" Відповідає протоколу: {is_valid}"
      )
    except Exception as e:
      print(f"ID: {sensor_id} Помилка читання: {e}")
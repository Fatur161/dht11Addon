import board
import adafruit_dht

# cвой GPIO-пин (например board.D27 = GPIO 27)
dhtDevice = adafruit_dht.DHT11(board.D4)

try:
    temperature_c = dhtDevice.temperature
    humidity = dhtDevice.humidity
    if humidity is not None and temperature_c is not None:
        print(f"Temp = {temperature_c:.1f}")
        print(f"Hum = {humidity:.1f}")
    else:
        print("Failed to read data")
except Exception as e:
    print("Error:", e)
finally:
    dhtDevice.exit()

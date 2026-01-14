# RPi-Monitor DHT11 Addon

## English

### Description

This addon integrates a DHT11 (or DHT22) temperature and humidity sensor with [RPi-Monitor](https://rpi-experiences.blogspot.com/p/rpi-monitor.html). It displays live temperature and humidity values and generates historical graphs via the RPi-Monitor web interface.

The system reads sensor data via a Python script and feeds it into RPi-Monitor using a Bash wrapper.

### Features

- Real-time display of ambient temperature and humidity
- Historical graphs with dual-axis for temperature and humidity
- Clean integration with RPi-Monitor pages

### File Structure

```
/usr/local/bin/
├── read_dht11.py # Python script that reads data from the DHT11 sensor
├── read_dht11.sh # Bash wrapper that calls the Python script
/etc/rpimonitor/
└── template/
└── dht11.conf # Configuration file for RPi-Monitor
```

### Requirements

- Raspberry Pi with DHT11 or DHT22 sensor connected
- Python 3
- Virtual environment at `/opt/dht-venv/` with the following packages installed:

```bash
pip install adafruit-circuitpython-dht
pip install adafruit-blinka
```

- libgpiod (required for Raspberry Pi, installed via sudo apt install libgpiod2 and libgpiod-dev if using C library)
- RPi-Monitor installed

Installation

1. Create a Python virtual environment:

```bash
python3 -m venv /opt/dht-venv
source /opt/dht-venv/bin/activate
pip install adafruit-circuitpython-dht adafruit-blinka
```

2. Copy files:

```bash
sudo cp read_dht11.py /usr/local/bin/
sudo cp read_dht11.sh /usr/local/bin/
sudo chmod +x /usr/local/bin/read_dht11.sh
sudo cp dht11.conf /etc/rpimonitor/template/
```

3. Restart RPi-Monitor:

```bash
sudo service rpimonitor restart
```

4. Open your browser and go to http://{raspberrypi_ip}:8888 - you should see a new "Bedroom" section with temperature and humidity readings.

## Русский

### Описание

Этот аддон позволяет интегрировать датчик температуры и влажности DHT11 (или DHT22) с RPi-Monitor. Он отображает текущие значения температуры и влажности, а также строит графики на веб-интерфейсе RPi-Monitor.

Считывание данных производится с помощью Python-скрипта, вызываемого через оболочку Bash.

### Возможности

- Отображение текущей температуры и влажности

- Исторические графики с двумя шкалами

- Полная интеграция с веб-интерфейсом RPi-Monitor

### Структура файлов

/usr/local/bin/
├── read_dht11.py # Python-скрипт для считывания данных с DHT11
├── read_dht11.sh # Bash-обёртка, вызывающая Python-скрипт
/etc/rpimonitor/
└── template/
└── dht11.conf # Конфигурация для RPi-Monitor

### Требования

- Raspberry Pi с подключённым DHT11 или DHT22
- Python 3
- Виртуальное окружение /opt/dht-venv/ с установленными пакетами:

```bash
pip install adafruit-circuitpython-dht
pip install adafruit-blinka
```

- libgpiod (требуется для Raspberry Pi, устанавливается через sudo apt install libgpiod2 и libgpiod-dev, если используется C-библиотека)
- Установленный RPi-Monitor

### Установка

1. Создайте виртуальное окружение Python:

```bash
python3 -m venv /opt/dht-venv
source /opt/dht-venv/bin/activate
pip install adafruit-circuitpython-dht adafruit-blinka
```

2. Скопируйте файлы:

```bash
sudo cp read_dht11.py /usr/local/bin/
sudo cp read_dht11.sh /usr/local/bin/
sudo chmod +x /usr/local/bin/read_dht11.sh
sudo cp dht11.conf /etc/rpimonitor/template/
```

3. Перезапустите RPi-Monitor:

```bash
sudo service rpimonitor restart
```

4. Откройте браузер и перейдите на http://{raspberrypi_ip}:8888 - вы увидите новый раздел "Bedroom" с показателями температуры и влажности.

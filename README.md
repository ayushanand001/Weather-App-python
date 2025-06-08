# Weather Forecast App

A simple Python desktop application that displays current weather information for any city using the OpenWeatherMap API. The app features a graphical user interface (GUI) built with Tkinter, allowing users to input a city name and view real-time weather details such as temperature, humidity, wind speed, and geographical coordinates.

---

## Features

- User-friendly Tkinter GUI
- Fetches real-time weather data from OpenWeatherMap
- Displays:
  - Latitude and Longitude
  - Temperature (current, min, max, feels like)
  - Humidity and Pressure
  - Wind Speed

---

## Installation

1. **Prerequisites:**  
   - Python 3.x installed on your system.

2. **Install required libraries:**  
   Open your terminal or command prompt and run:
   '''
   pip install requests
   '''  
*Tkinter is included with standard Python installations. If you encounter issues, install it using:*
- For Ubuntu/Debian:
  ```
  sudo apt-get install python3-tk
  ```
- For Fedora:
  ```
  sudo yum install python3-tkinter tk-devel
  ```

---

## Usage

1. **Clone the repository:**
git clone https://github.com/yourusername/weather-forecast-app.git
cd weather-forecast-app

2. **Set your OpenWeatherMap API key:**  
Replace `YOUR_API_KEY` in the code with your actual OpenWeatherMap API key (see [API Key Setup](#api-key-setup)).

3. **Run the application:**
'''
python main.py
'''

5. **How it works:**  
- Enter a city name in the input field.
- Click the "show" button.
- Weather details for the city will be displayed in the app window.

---

## API Key Setup

This app uses the OpenWeatherMap API, which requires a free API key.

1. Sign up at [OpenWeatherMap](https://openweathermap.org/api) to get your API key.
2. In the code, find the line:
'''
response = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={cityname}&appid=YOUR_API_KEY')
'''
4. Replace `YOUR_API_KEY` with your actual API key.

---

## Tech Stack

- Python 3.x
- Tkinter (GUI)
- Requests (HTTP requests)
- [OpenWeatherMap API](https://openweathermap.org/api)

---

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request with your improvements or bug fixes.

---

## License

This project is licensed under the MIT License.

---

_Last updated: June 8, 2025_


# Simple Weather App

A beginner-friendly desktop weather application built with Python that fetches real-time weather data and displays it in a modern, user-friendly interface.

![Weather App Screenshot](https://img.shields.io/badge/Python-3.7+-blue.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)

## Table of Contents
- [About the Project](#about-the-project)
- [Features](#features)
- [What I Learned](#what-i-learned)
- [Technologies Used](#technologies-used)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [API Setup](#api-setup)
- [Project Structure](#project-structure)
- [Key Concepts Demonstrated](#key-concepts-demonstrated)
- [Challenges Faced](#challenges-faced)
- [Future Improvements](#future-improvements)
- [Contributing](#contributing)

## About the Project

This is a desktop weather application that allows users to search for current weather conditions in any city worldwide. The app features a modern dark theme interface and displays weather information including temperature, weather description, and weather icons.

The project was built as a learning exercise to understand:
- API integration and HTTP requests
- GUI development with Python
- Error handling and user experience
- Modern UI design principles

## Features

- 🔍 **City Search**: Search for weather in any city worldwide
- 🌡️ **Real-time Data**: Displays current temperature in Celsius
- 🌤️ **Weather Icons**: Visual weather icons from OpenWeatherMap
- 🎨 **Modern UI**: Dark theme with clean, professional design
- ⚡ **Keyboard Support**: Press Enter to search
- 🏙️ **Default Location**: Loads Stockholm weather on startup
- 🚨 **Error Handling**: User-friendly error messages for invalid cities or API issues

## What I Learned

### Programming Concepts
- **API Integration**: How to make HTTP requests to external APIs and handle responses
- **JSON Data Handling**: Parsing and extracting data from JSON responses
- **Error Handling**: Implementing proper error handling for different scenarios (404, 401, 500 errors)
- **GUI Development**: Creating desktop applications with tkinter and modern styling with ttkbootstrap
- **Event Handling**: Responding to user interactions (button clicks, keyboard input)
- **Image Handling**: Downloading and displaying images from URLs

### Software Development Skills
- **Code Organization**: Separating concerns with different functions for different tasks
- **User Experience**: Designing intuitive interfaces and providing helpful feedback
- **Environment Management**: Using virtual environments for Python projects
- **Documentation**: Writing clear, comprehensive documentation

### Problem-Solving Approaches
- **API Documentation Reading**: Learning to read and understand API documentation
- **Debugging**: Troubleshooting import errors and dependency issues
- **UI/UX Design**: Creating visually appealing and functional interfaces

## Technologies Used

- **Python 3.7+**: Main programming language
- **tkinter**: Built-in Python GUI framework
- **ttkbootstrap**: Modern themes and styling for tkinter
- **requests**: HTTP library for API calls
- **OpenWeatherMap API**: Weather data source
- **JSON**: Data format for API responses

## Prerequisites

Before running this project, make sure you have:

- Python 3.7 or higher installed
- pip (Python package installer)
- Internet connection (for API calls)
- OpenWeatherMap API key (free registration required)

## Installation

1. **Clone or download the project**
   ```bash
   git clone <your-repo-url>
   cd WeatherApp
   ```

2. **Create a virtual environment** (recommended)
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install required packages**
   ```bash
   pip3 install requests ttkbootstrap
   ```

4. **Get your API key**
   - Visit [OpenWeatherMap](https://openweathermap.org/api)
   - Sign up for a free account
   - Get your API key from the dashboard

5. **Update the API key**
   - Open `main.py`
   - Replace the API_KEY value with your own key:
     ```python
     API_KEY = "your_api_key_here"
     ```

## 💻 Usage

1. **Run the application**
   ```bash
   python3 main.py
   ```

2. **Using the app**
   - The app will start showing weather for Stockholm by default
   - Type any city name in the search box
   - Click "Search" or press Enter
   - View the current weather information

## API Setup

This project uses the OpenWeatherMap API:

1. **Sign up**: Create a free account at [OpenWeatherMap](https://openweathermap.org/api)
2. **Get API Key**: Find your API key in your account dashboard
3. **Update Code**: Replace the API_KEY variable in `main.py`
4. **API Limits**: Free tier allows 1,000 calls per day

**Important**: Never commit your real API key to version control. Consider using environment variables for production applications.

## Project Structure

```
WeatherApp/
├── main.py          # Main application file
├── README.md        # Project documentation
├── venv/           # Virtual environment (not tracked in git)
└── requirements.txt # Dependencies
```

## Key Concepts Demonstrated

### 1. **API Integration**
```python
def get_weather_data(city):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)
```

### 2. **Error Handling**
```python
if response.status_code == 404:
    Messagebox.show_error("City not found", "Error")
    return None
```

### 3. **GUI Layout**
```python
main_frame = ttk.Frame(root, padding=30)
main_frame.pack(fill="both", expand=True)
```

### 4. **Event Binding**
```python
city_entry.bind("<Return>", lambda e: search())
```

## Challenges Faced

1. **Import Errors**: Learned about Python package management and virtual environments
2. **API Key Management**: Understanding the importance of keeping API keys secure
3. **UI Design**: Balancing functionality with visual appeal
4. **Error Handling**: Providing meaningful feedback to users
5. **Image Loading**: Handling dynamic image loading from URLs

## Future Improvements

- [ ] Add 5-day weather forecast
- [ ] Implement geolocation for automatic city detection
- [ ] Add temperature unit conversion (Celsius/Fahrenheit)
- [ ] Save favorite cities
- [ ] Add weather alerts and notifications
- [ ] Implement offline mode with cached data
- [ ] Add more detailed weather information (humidity, wind speed, etc.)
- [ ] Create a web version using Flask
- [ ] Add weather maps integration

## Contributing

This is a learning project, but suggestions and improvements are welcome! Feel free to:

1. Fork the project
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## License

This project is open source and available under the [MIT License](LICENSE).

## Acknowledgments

- [OpenWeatherMap](https://openweathermap.org/) for providing the weather API
- [ttkbootstrap](https://ttkbootstrap.readthedocs.io/) for modern tkinter themes
- Python community for excellent documentation and resources

---


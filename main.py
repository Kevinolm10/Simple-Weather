import requests
import json
import os
import datetime


API_KEY = "319411e71d70d6546b85d548e53e4c7c"
city = "Stockholm"
url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"


response = requests.get(url)
data = response.json()

print(data)
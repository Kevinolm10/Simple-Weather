import requests
import json
import tkinter as tk
import ttkbootstrap
from ttkbootstrap.dialogs import Messagebox

API_KEY = "319411e71d70d6546b85d548e53e4c7c"

def get_weather_data(city):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)

    if response.status_code == 404:
        Messagebox.showerror("Error", "City not found")
        return None
    elif response.status_code == 401:
        Messagebox.showerror("Error", "Invalid API key")
        return None
    elif response.status_code == 500:
        Messagebox.showerror("Error", "Server error")
        return None
    else:
        weather = response.json()
        icon_id = weather['weather'][0]['icon']
        temperature = weather['main']['temp']
        description = weather['weather'][0]['description']
        city_name = weather['name']
        country = weather['sys']['country']
        icon_url = f"https://openweathermap.org/img/wn/{icon_id}.png"
        return (icon_url, temperature, description, city_name, country)

def update_weather_display(icon_url, temperature, description, city_name, country):
    location_label.config(text=f"Location: {city_name}, {country}")
    temperature_label.config(text=f"Temperature: {temperature}°C")
    description_label.config(text=f"Description: {description}")

    icon_data = requests.get(icon_url).content
    icon_image = tk.PhotoImage(data=icon_data)
    icon_label.config(image=icon_image)
    icon_label.image = icon_image

def search():
    city = city_entry.get()
    result = get_weather_data(city)
    if result:
        update_weather_display(*result)

# Root windows settings
root = tk.Tk()
root.title = "Weather App"
root.geometry("600x400")
root.configure(bg='blue')

frame = tk.Frame(root, bg='white', bd=2, relief='groove', padx=20, pady=20)
frame.pack(padx=30, pady=30)

city_entry = ttkbootstrap.Entry(frame, width=30, font=("Arial", 12))
city_entry.pack(pady=10)

search_button = ttkbootstrap.Button(frame, text="Search", bootstyle="primary", command=search)
search_button.pack(pady=10)

icon_label = tk.Label(frame)
icon_label.pack(pady=5)

location_label = ttkbootstrap.Label(root, font=("Arial", 14))
location_label.pack(pady=10)

temperature_label = ttkbootstrap.Label(root, font=("Arial", 12))
temperature_label.pack(pady=5)

description_label = ttkbootstrap.Label(root, font=("Arial", 12))
description_label.pack(pady=5)

# Load initial data for Stockholm
result = get_weather_data("Stockholm")
if result:
    update_weather_display(*result)

root.mainloop()

import requests
import json
import tkinter as tk
import ttkbootstrap as ttk
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
    location_label.config(text=f"{city_name}, {country}")
    temperature_label.config(text=f"{temperature}°C")
    description_label.config(text=description.title())

    icon_data = requests.get(icon_url).content
    icon_image = tk.PhotoImage(data=icon_data)
    icon_label.config(image=icon_image)
    icon_label.image = icon_image

def search():
    city = city_entry.get()
    if city.strip():
        result = get_weather_data(city)
        if result:
            update_weather_display(*result)

# Root window with modern theme
root = ttk.Window(themename="superhero")
root.title("Weather App")
root.geometry("500x600")
root.resizable(False, False)

# Main container
main_frame = ttk.Frame(root, padding=30)
main_frame.pack(fill="both", expand=True)

# Title
title_label = ttk.Label(main_frame, text="Weather App", font=("Arial", 24, "bold"))
title_label.pack(pady=(0, 30))

# Search section
search_frame = ttk.Frame(main_frame)
search_frame.pack(fill="x", pady=(0, 30))

city_entry = ttk.Entry(search_frame, font=("Arial", 14), width=25)
city_entry.pack(side="left", padx=(0, 10), fill="x", expand=True)

search_button = ttk.Button(search_frame, text="Search", bootstyle="primary", command=search)
search_button.pack(side="right")

# Weather display card
weather_card = ttk.Frame(main_frame, padding=20, relief="solid", borderwidth=1)
weather_card.pack(fill="x", pady=(0, 20))

# Icon and location
header_frame = ttk.Frame(weather_card)
header_frame.pack(fill="x", pady=(0, 15))

icon_label = ttk.Label(header_frame)
icon_label.pack(side="left", padx=(0, 15))

location_label = ttk.Label(header_frame, font=("Arial", 18, "bold"))
location_label.pack(side="left", anchor="w")

# Temperature
temperature_label = ttk.Label(weather_card, font=("Arial", 36, "bold"), bootstyle="primary")
temperature_label.pack(pady=(0, 10))

# Description
description_label = ttk.Label(weather_card, font=("Arial", 14))
description_label.pack()

# Bind Enter key to search
city_entry.bind("<Return>", lambda e: search())

# Load initial data for Stockholm
result = get_weather_data("Stockholm")
if result:
    update_weather_display(*result)

root.mainloop()

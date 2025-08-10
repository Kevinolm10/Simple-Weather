import requests
import json
import tkinter as tk

API_KEY = "319411e71d70d6546b85d548e53e4c7c"
city = "Stockholm"
url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

root = tk.Tk()
root.geometry("600x400")
root.configure(bg='blue')

frame = tk.Frame(root, bg='white', bd=2, relief='groove', padx=20, pady=20)
frame.pack(padx=30, pady=30)

response = requests.get(url)
data = response.json()

print(json.dumps(data, indent=2))

name = data.get('name', 'N/A')
temp = data.get('main', {}).get('temp', 'N/A')
weather_desc = data.get('weather', [{}])[0].get('description', 'N/A')

tk.Label(frame, text=f"City: {name}", bg='white', font=("Arial", 14)).pack(anchor='w')
tk.Label(frame, text=f"Temperature: {temp} °C", bg='white', font=("Arial", 14)).pack(anchor='w')
tk.Label(frame, text=f"Weather: {weather_desc}", bg='white', font=("Arial", 14)).pack(anchor='w')

root.mainloop()

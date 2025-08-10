import requests
import tkinter as tk
from tkinter import ttk

API_KEY = "319411e71d70d6546b85d548e53e4c7c"
city = "Stockholm"
url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

root = tk.Tk()
root.title("Weather App")
root.geometry("800x600")
root.resizable(True, True)
root.configure(bg="lightblue")

root.mainloop()


response = requests.get(url)
data = response.json()

print(data)

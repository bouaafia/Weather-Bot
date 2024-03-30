import requests
import tkinter as tk
from tkinter import simpledialog
from tkinter import messagebox
# Go to openweathermap and create a account and get an api key and enter it here
api = ""
def GetWeather(city , apikey):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={apikey}"
    response = requests.get(url)
    data = response.json()
    if response.status_code == 200 :
        weather_description = data['weather'][0]['description']
        temperature = data['main']['temp']
        temperature_celsius = temperature - 273.15
        return {
            'description': weather_description,
            'temperature': temperature_celsius,
        }
    else :
         return None
def GetValue():
    value = simpledialog.askstring("Weather", "Enter the city that you want ")
    info = GetWeather(city=value , apikey=api)
    if info :
        messagebox.showinfo(title=value , message=f"Description : {info['description']} \nTemperature : {info['temperature']:.2f}°C")
    else :
        messagebox.showerror(title=value , message='city was not found')

GetValue()

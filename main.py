# Import all dependencies
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import telegram_send
from datetime import datetime
import time
import requests, json

anniversaire = 1
day = datetime.now().strftime('%A')
year = datetime.now().strftime('%Y')
date = datetime.now().strftime('%d-%m')
Heure = datetime.now().strftime('%H:%M:%S')
weather = "none"

#print(f"La date est le {date}")
#print(f"L'heure est {Heure}")

def weather_valence():
    # base URL
    BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"
    CITY = "Valence"
    API_KEY = "a3288f06585e9ccc42df1b71d2718e6f"
    # upadting the URL
    URL = BASE_URL + "q=" + CITY + "&appid=" + API_KEY
    # HTTP request
    response = requests.get(URL)
    # checking the status code of the request
    if response.status_code == 200:
       # getting data in the json format
       data = response.json()
       # getting the main dict block
       main = data['main']
       # getting temperature
       temperature = main['temp']
       # getting the humidity
       humidity = main['humidity']
       # getting the pressure
       pressure = main['pressure']
       # weather report
       report = data['weather']
       print(f"{CITY:-^30}")
       telegram_send.send(messages=[f"A Valence il fait actuellement {temperature} degrees avec un temps dit {report[0]['description']}]")
       #print(f"Temperature: {temperature}")
       #print(f"Humidity: {humidity}")
       #print(f"Pressure: {pressure}")
       #print(f"Weather Report: {report[0]['description']}")
    else:
       # showing the error message
       print("Error in the HTTP request")
        
        
        
        
        
        
 def weather_romans():
    # base URL
    BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"
    CITY = "Romans-Sur-Isere"
    API_KEY = "a3288f06585e9ccc42df1b71d2718e6f"
    # upadting the URL
    URL = BASE_URL + "q=" + CITY + "&appid=" + API_KEY
    # HTTP request
    response = requests.get(URL)
    # checking the status code of the request
    if response.status_code == 200:
       # getting data in the json format
       data = response.json()
       # getting the main dict block
       main = data['main']
       # getting temperature
       temperature = main['temp']
       # getting the humidity
       humidity = main['humidity']
       # getting the pressure
       pressure = main['pressure']
       # weather report
       report = data['weather']
       print(f"{CITY:-^30}")
       telegram_send.send(messages=[f"A Romans il fait actuellement {temperature} degrees avec un temps dit {report[0]['description']}]")
       #print(f"Temperature: {temperature}")
       #print(f"Humidity: {humidity}")
       #print(f"Pressure: {pressure}")
       #print(f"Weather Report: {report[0]['description']}")
    else:
       # showing the error message
       print("Error in the HTTP request")

while True:

    time.sleep()
    weather_valence(3600)
    weather_romans(3600)
    
    
    if date == '18-08':
        if anniversaire == 0:
            telegram_send.send(messages=[f"Bon anniversaire monsieur pour ce {2022-2000}eme anniversaire"])
            anniversaire = 1
    if date == '19-08':
        anniversaire = 1
#    else:
#        print("Aujourd'hui on est pas le 16 aout")

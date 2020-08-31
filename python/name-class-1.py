# Finn Lestrange - 2020
# Name program

# https://www.geeksforgeeks.org/python-find-current-weather-of-any-city-using-openweathermap-api/ - This is where I got the weather API code

from datetime import date, datetime
import json
import requests
api_key = "125ae9807f4b8f5b0bacd1398d102070"
url = "http://api.openweathermap.org/data/2.5/weather?"


today = date.today()
senior = datetime(2022, 8, 21)
senior_year = senior - datetime.now()
senior_string = str(senior_year)
name = input('What is your name? ')
city = input("What city do you live in? ")




print("Hello " + name + "! Todays date is " + str(today) +". It is " + senior_string[:8] + " until you are a senior! The weather today is:")

### Code from https://www.geeksforgeeks.org/python-find-current-weather-of-any-city-using-openweathermap-api/
complete_url = url + "appid=" + api_key + "&q=" + city
response = requests.get(complete_url)
json_convert = response.json()



if json_convert["cod"] != "404":
    # store the value of "main"
    # key in variable y
    y = json_convert["main"]
    # store the value corresponding
    # to the "temp" key of y
    current_temperature = y["temp"]
    # store the value corresponding
    # to the "pressure" key of y
    current_pressure = y["pressure"]
    # store the value corresponding
    # to the "humidity" key of y
    current_humidiy = y["humidity"]
    # store the value of "weather"
    # key in variable z
    z = json_convert["weather"]
    # store the value corresponding
    # to the "description" key at
    weather_description = z[0]["description"]

    # print following values
    print("The weather in " + city + " city today is:")
    print(" Temperature = " + str("{:.2f}".format(round(current_temperature, 2) - 273.15)) + " degrees Celsius ")
    print("\n Atmospheric pressure is " + str(current_pressure) + "hPa")
    print("\n Humidity is " + str(current_humidiy) + "%")
    print("\n Weather description = " + str(weather_description))
else:
    print(" City Not Found ")

## Extension still Undecided - Would quite like to incorperate anoteher API as this was my first time using an api to get data into a python program ##

import requests
import os
from datetime import datetime

user_api = os.environ['current_weather_data']
location = input("Enter the city name: ")
# Passed from website: api.openweathermap.org/data/2.5/weather?q=(city name)&appid=(api key)

complete_api_link = "https://api.openweathermap.org/data/2.5/weather?q="+location+"&appid="+user_api

api_link = requests.get(complete_api_link)
api_data = api_link.json()

if api_data['cod'] == '404':
    print("Invalid City: {}, Please check the city name".format(location))
else:
    #create vars to store and display data
    temp_city_f = (((api_data['main']['temp']) - 273.15) * 2 + 30)
    temp_city_c = ((api_data['main']['temp']) - 273.15)
    feels_like_c = ((api_data['main']['feels_like']) - 273.15)
    feels_like_f = (((api_data['main']['feels_like']) - 273.15) * 2 + 30)
    weather_description = api_data['weather'][0]['description']
    humidity = api_data['main']['humidity']
    wind_speed = api_data['wind']['speed']
    date_time = datetime.now().strftime("%d %b %y | %I:%M:%S %p")

    high_c = ((api_data['main']['temp_max']) - 273.15)
    low_c = ((api_data['main']['temp_min']) - 273.15)
    high_f = (((api_data['main']['temp_max']) - 273.15) * 2 + 30)
    low_f = (((api_data['main']['temp_min']) - 273.15) * 2 + 30)

    print("------------------------------------------------------------")
    print("Weather Stats for - {} || {}".format(location.upper(), date_time))
    print("------------------------------------------------------------")

    print("Current temperature is: {:.2f} deg F | {:.2f} deg C".format(temp_city_f, temp_city_c))
    print("Current Humidity      :", humidity, '%')
    print("Current Wind-Speed    :", wind_speed, 'kmph')
    print("Weather Description   :", weather_description)
    print('*' * 50)
    print("Feels like            : {:.2f} deg F | {:.2f} deg C".format(feels_like_f, feels_like_c))
    print("High for Today        : {:.2f} deg F | {:.2f} deg C".format(high_f, high_c))
    print("Low for Today         : {:.2f} deg F | {:.2f} deg C".format(low_f, high_c))
    input()

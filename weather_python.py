#Author : Anuraj R

import requests
import time
api_key = "735364377dea461e983161109240911"
base_url = "http://api.weatherapi.com/v1/current.json"
print("weather  checker")
print(" ")
location=input("enter the place you want check the weather \n ")
if(location==" "):
	print("please enter the place")
else:
	print("Analysing current ...")
	time.sleep(5)
	print("check Cloudy or not..")
	time.sleep(5)
	print("checking .....")
	print("processing status ...")
	time.sleep(5)
	print(f"checking current status of {location}")
	time.sleep(6)
	print(" ")
response = requests.get(f"{base_url}?key={api_key}&q={location}")
if response.status_code == 200:
    data = response.json()
    # Getting the details from api
    temperature = data["current"]["temp_c"]
    condition = data["current"]["condition"]["text"]
    humidity = data["current"]["humidity"]
    pressure = data["current"]["pressure_mb"]
    cloudiness = data["current"]["cloud"]
    wind_speed = data["current"]["wind_kph"]

    # Print the weather details
    print(f"The weather in {location}:")
    print(f"Temperature: {temperature}°C")
    print(f"Condition: {condition}")
    print(f"Humidity: {humidity}%")
    print(f"Pressure: {pressure} mb")
    print(f"Cloudiness: {cloudiness}%")
    print(f"Wind Speed: {wind_speed} kph")
else:
    print("Failed to retrieve weather data.")

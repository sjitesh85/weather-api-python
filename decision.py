# the Open weather API


import requests

#54.685500, 25.287539 - cathedral square
weather = requests.get(url="https://api.openweathermap.org/data/2.5/weather?lat=54.685500&lon=25.287539&units=metric&appid=cf5781a1d377581680898bcb7d5e0d5c")
weather.raise_for_status()

data = weather.json()

temp = weather.json()["main"]["temp"]
print("So, the current temperature is: ", temp)



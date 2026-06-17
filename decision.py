# the Open weather API

import datetime 
import requests
x = requests.get(url="https://api.openweathermap.org/data/2.5/weather?lat=54.6845&lon=25.2858&units=metric&appid=cf5781a1d377581680898bcb7d5e0d5c")
print(x)
print("hi") 

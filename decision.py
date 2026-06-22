# the Open weather API


import requests
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("API_KEY")

#54.685500, 25.287539 - cathedral square
weather = requests.get(url=f"https://api.openweathermap.org/data/2.5/weather?lat=54.685500&lon=25.287539&units=metric&appid={api_key}")
weather.raise_for_status()

#data = weather.json()

temp = weather.json()["main"]["temp"]

import random
# Fixed pant options
pant_options = ["Black Jeans", "Blue Jeans", "Brown Pant", "Olive pant", "Grey Jeans"]
light_jackets = ["Denim jacket", "Black Jacket", "Brown Jacket", "Red Jacket"]

# Random Shirt/T-shirt options
if temp < 10:
    top_options = ["Black Hoddie", "Red Hoddie", "Green Hoddie"]
    jacket_required = True
    jacket = "Heavy jacket"
elif 10<= temp < 20:
    top_options = ["Blue Shirt", "Yellow Shirt", "Black Shirt"]
    jacket_required = True
    jacket = random.choice(light_jackets)
else:
    top_options = ["Black T-Shirt", "Olive T-Shirt", "White T-Shirt", "Blue T-Shirt", "Grey T-Shirt"]
    jacket_required = False
    jacket = None

# randomizer
top = random.choice(top_options)
pant = random.choice(pant_options)

if jacket_required:
    outfit = (top, jacket, pant)
else:
    outfit = (top, pant)



# Output 
print("Hey Jitesh, the current outside temperature is: ", temp, " c")
print(f"And yours today's Outfit is : {outfit}")


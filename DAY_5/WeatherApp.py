# Day 5(09-03-2024)
# Weather App

import requests
import json

city = input("Enter the name of the city\n")

url = f"https://api.weatherapi.com/v1/current.json?key=b13989793f184149a91141538230103&q={city}"

r = requests.get(url)
# to convert in stringhe
wDic = json.loads(r.text)
w = wDic["current"]["temp_c"]
print(w)
import certifi
from pymongo import MongoClient
import requests
import pandas as pd

var = certifi.where()

mongo_client = MongoClient("mongodb+srv://JHX:DBAdmin123@cluster0.2h1wwcv.mongodb.net/?retryWrites=true&w=majority", tlsCAFile=var)
db = mongo_client["Weather"]
db.weather.drop()


weather_api_key = "2045ca032793d4b29b3dd67358c2395d"

url = "http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=" + weather_api_key


df = pd.read_csv("./Vacation_Search/worldcities.csv")

cities = list(df['city'])

for city in cities:

    city_url = url + "&q=" + city.replace(" ","+")

    try:
        city_weather = requests.get(city_url).json()

        city_lat = city_weather["coord"]["lat"]
        city_lng = city_weather["coord"]["lon"]
        city_max_temp = city_weather["main"]["temp_max"]
        city_humidity = city_weather["main"]["humidity"]
        city_clouds = city_weather["clouds"]["all"]
        city_wind = city_weather["wind"]["speed"]
        city_country = city_weather["sys"]["country"]

        # print("City details found...")

        db.weather.insert_one({"City": city.title(),
                    "Lat": city_lat,
                    "Lng": city_lng,
                    "Max Temp": city_max_temp,
                    "Humidity": city_humidity,
                    "Cloudiness": city_clouds,
                    "Wind Speed": city_wind,
                    "Country": city_country})

    except:
        # print("City not found. Skipping...")
        pass

print("Insertion Successful!")
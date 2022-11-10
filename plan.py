from dis import dis
import folium
from pymongo import MongoClient
import certifi
import haversine as hs
import webbrowser

class Plan:
    
    def getItinerary(min_temp = 75, max_temp = 90, city = "Delhi", distance = 50):

        print(min_temp, max_temp, city, distance)

        C = certifi.where()

        mongo_client = MongoClient("mongodb+srv://JHX:DBAdmin123@cluster0.2h1wwcv.mongodb.net/?retryWrites=true&w=majority", tlsCAFile=C)
        db = mongo_client["Weather"]

        myquery = {"City": { "$eq": city } }
        result = db.weather.find(myquery)

        city = list(result)[0]
        loc1 = (city['Lat'], city['Lng'])

        cities = []

        myquery = { "Max Temp": { "$gte": min_temp, "$lte": max_temp } }

        result = db.weather.find(myquery)
        result = list(result)

        for city in result:
            loc2 = (city['Lat'], city['Lng'])

            if hs.haversine(loc1,loc2) <= distance:
                cities.append(city)

        print(len(cities))

        m = folium.Map(location=loc1, zoom_start=9)

        for i in range(0, len(cities)):
            folium.Marker(
            location=[cities[i]['Lat'], cities[i]['Lng']],
            popup=cities[i],
            ).add_to(m)

        m.save('map.html')

        webbrowser.open("map.html")

        return ""




















# api_key = "AIzaSyDJAJrvacy64DHyikmqBKf-D9gx6kK1mIw"


# for index, row in df.iterrows():

#     url = "https://maps.googleapis.com/maps/api/place/nearbysearch/json?location="
#     lat = row["Lat"]

#     url += str(lat)+"%2C"
#     lon = row["Lng"]
    
#     url += str(lon)+"&radius=5000&type=lodging&key=AIzaSyDJAJrvacy64DHyikmqBKf-D9gx6kK1mIw"

#     payload={}
#     headers = {}

#     response = requests.request("GET", url, headers=headers, data=payload)

#     print(response.text)






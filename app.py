from turtle import distance
from flask import Flask, render_template, url_for, request, jsonify
from plan import Plan

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def process():
    data = request.form
    
    name = data['name']
    city = data['loc']
    minTemp = data['mintemp']
    maxTemp = data['maxtemp']
    distance = data['distance']
    visits = data['visits']

    Plan.getItinerary(int(minTemp), int(maxTemp), city, int(distance))

    return "Itinerary displayed!"


if __name__ == "__main__":
    app.run(debug = True)



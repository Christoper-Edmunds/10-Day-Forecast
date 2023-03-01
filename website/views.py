from flask import Blueprint, render_template , request
from .models import weatherdatabase
from . import db
import geocoder
import requests 
import datetime

views = Blueprint('views', __name__)

@views.route('/', methods=['GET', 'POST'])
def home():
    #gets current latitude and longitude
    data =  geocoder.ip('me')
    print(data.latlng)

    #builds api query using latitude and longitude
    modifiedApiString = ("https://api.open-meteo.com/v1/forecast?latitude=" + str(data.latlng[0]) + "&longitude=" + str(data.latlng[1]) + "&hourly=temperature_2m,rain,windspeed_10m")

    #prepares json object from api call 
    response = requests.get(modifiedApiString)
    rawJson = response.json()

    #prepares date time string
    currentDT = datetime.datetime.now()
    datetimeString = (str(currentDT.hour) + " : " + str(currentDT.minute))


    hour1value = rawJson['hourly']['temperature_2m'][0]
    hour2value = rawJson['hourly']['temperature_2m'][1]
    hour3value = rawJson['hourly']['temperature_2m'][2]
    hour4value = rawJson['hourly']['temperature_2m'][3]
    hour5value = rawJson['hourly']['temperature_2m'][4]
    hour6value = rawJson['hourly']['temperature_2m'][5]
    hour7value = rawJson['hourly']['temperature_2m'][6]
    hour8value = rawJson['hourly']['temperature_2m'][7]
    hour9value = rawJson['hourly']['temperature_2m'][8]
    hour10value = rawJson['hourly']['temperature_2m'][9] 

    rain1value = rawJson['hourly']['rain'][0]
    rain2value = rawJson['hourly']['rain'][1]
    rain3value = rawJson['hourly']['rain'][2]
    rain4value = rawJson['hourly']['rain'][3]
    rain5value = rawJson['hourly']['rain'][4]
    rain6value = rawJson['hourly']['rain'][5]
    rain7value = rawJson['hourly']['rain'][6]
    rain8value = rawJson['hourly']['rain'][7]
    rain9value = rawJson['hourly']['rain'][8]
    rain10value = rawJson['hourly']['rain'][9] 

    windSpeed1value = rawJson['hourly']['windspeed_10m'][0]
    windSpeed2value = rawJson['hourly']['windspeed_10m'][1]
    windSpeed3value = rawJson['hourly']['windspeed_10m'][2]
    windSpeed4value = rawJson['hourly']['windspeed_10m'][3]
    windSpeed5value = rawJson['hourly']['windspeed_10m'][4]
    windSpeed6value = rawJson['hourly']['windspeed_10m'][5]
    windSpeed7value = rawJson['hourly']['windspeed_10m'][6]
    windSpeed8value = rawJson['hourly']['windspeed_10m'][7]
    windSpeed9value = rawJson['hourly']['windspeed_10m'][8]
    windSpeed10value = rawJson['hourly']['windspeed_10m'][9] 

    latitude = data.latlng[0]
    longitude = data.latlng[1]

    userGreeting = "error"

    table_data = weatherdatabase.query.filter_by(latitude=latitude, longitude=longitude).all()
    if len(table_data) != 0:
        userGreeting = ("Welcome Back User At | Latitude: " + str(latitude) + " " + "| Longitude: " + str(longitude))
        print (userGreeting)
    else:
        userGreeting = ("Welcome New User At | Latitude: " + str(latitude) + " " + "| Longitude: " + str(longitude))
        print ("New User!")
        new_user = weatherdatabase(latitude=latitude, longitude=longitude)
        db.session.add(new_user)
        db.session.commit()

    return render_template("home.html", datetimeString = datetimeString, userGreeting = userGreeting ,hour1value = hour1value, hour2value = hour2value, hour3value = hour3value, hour4value = hour4value, hour5value = hour5value, hour6value = hour6value, hour7value = hour7value, hour8value = hour8value, hour9value = hour9value, hour10value = hour10value, rain1value = rain1value, rain2value = rain2value, rain3value = rain3value, rain4value = rain4value, rain5value = rain5value, rain6value = rain6value, rain7value = rain7value, rain8value = rain8value, rain9value = rain9value, rain10value = rain10value, windSpeed1value = windSpeed1value, windSpeed2value = windSpeed2value, windSpeed3value = windSpeed3value, windSpeed4value = windSpeed4value, windSpeed5value = windSpeed5value, windSpeed6value = windSpeed6value, windSpeed7value = windSpeed7value, windSpeed8value = windSpeed8value, windSpeed9value = windSpeed9value, windSpeed10value = windSpeed10value)

@views.route('/info')
def info():
    return render_template("info.html")

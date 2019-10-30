from flask import render_template, Blueprint, jsonify
import pyowm
from datetime import datetime
import os
import requests
from bs4 import BeautifulSoup
from random import sample
import wikipedia


# TODO: implement JS for get_historic_events
# TODO: set init js methods as async

home_helper = Blueprint("home_helper", __name__)
open_weather_api_key = os.environ.get('OPEN_ENV_KEY')
OWM = pyowm.OWM(open_weather_api_key)

# Change for your needs
USER_NAME = 'Ariel + Scott + Gracie'  # for welcome message
BREED = ['retriever', 'golden']  # dog breed image to see
CITY_COORDS = {'lat': 42.313250, 'lon': -71.114173} # get your city's latitude & longitude


# VIEWS
@home_helper.route('/', methods=['GET'])
def home():
    return render_template('home.html', user_name=USER_NAME)


# API Endpoints

@home_helper.route('/get_historic_events', methods=['GET'])
def get_historic_events():
    date = datetime.now()
    date = date.strftime('%B') + ' ' + str(date.day)
    page = wikipedia.WikipediaPage(date)
    soup = BeautifulSoup(page.html())
    events = soup.find("span", id="Events").find_next("ul").find_all("li")
    events = [i.text for i in events]
    events = sample([i for i in events if len(i) < 108], 3)  # limit event text length bc/ screen size
    print(events)
    return jsonify({'events': events}), 200


@home_helper.route('/get_weather', methods=['GET'])
def get_weather():
    weather = OWM.weather_at_coords(CITY_COORDS['lat'], CITY_COORDS['lon']).get_weather()
    resp = dict()
    resp['temperature'] = weather.get_temperature(unit='fahrenheit')
    resp['wind'] = str(weather.get_wind()['speed'])  # meters/sec
    resp['detailed_status'] = weather.get_detailed_status()
    sunset = datetime.fromtimestamp(weather.get_sunset_time())
    hour = str(sunset.hour - 12) if sunset.hour > 12 else str(sunset.hour)
    minute = '0' + str(sunset.minute) if sunset.minute < 10 else str(sunset.minute)
    resp['sunset'] = hour + ':' + minute + 'pm'
    print(resp)
    return jsonify(resp), 200


@home_helper.route('/get_dog_pic', methods=['GET'])
def get_dog_pic():
    dog_img = requests.get('https://dog.ceo/api/breed/{}/{}/images/random'.format(BREED[0], BREED[1]))
    img_url = dog_img.json()['message']
    return jsonify({'img_url': img_url}), 200


@home_helper.route('/get_quote', methods=['GET'])
def get_quote():
    quote = requests.get('http://quotes.rest/qod.json').json()
    quote = quote['contents']['quotes'][0]
    return jsonify({'quote': quote['quote'], 'author': quote['author']}), 200

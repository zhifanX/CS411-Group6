import requests
import configparser


def get_api_key():
    config = configparser.ConfigParser()
    config.read('config.ini')
    return config['openweathermap']['api']

def get_weather(zip, api_key):
    api_url = "http://api.openweathermap.org/data/2.5/weather?zip={}&units=imperial&appid={}".format(zip, api_key)
    r = requests.get(api_url)
    return r.json()

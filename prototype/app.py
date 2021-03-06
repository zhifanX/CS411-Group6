from flask import Flask, render_template, request
import requests
import configparser

app = Flask(__name__)

@app.route('/')
def weather_search():
    return render_template('home.html')

@app.route('/results', methods = ['POST'])
def results():
    zip_code = request.form['zipcode']
    api_key = get_api_key()
    data = get_weather(zip_code, api_key)
    temp = int(data['main']['temp'])
    weather = data["weather"][0]["main"]
    location = data["name"]
    return render_template('results.html', location = location, temp = temp, weather = weather)


def get_api_key():
    config = configparser.ConfigParser()
    config.read('config.ini')
    return config['openweathermap']['api']

def get_weather(zip, api_key):
    api_url = "http://api.openweathermap.org/data/2.5/weather?zip={}&units=imperial&appid={}".format(zip, api_key)
    r = requests.get(api_url)
    return r.json()

if __name__ == '__main__':
    app.run()

from flask import Flask, render_template, request
from util import weather_api
from util import yelp_api

app = Flask(__name__)

@app.route('/')
def weather_search():
    return render_template('home.html')

@app.route('/results', methods = ['POST'])
def results():
    zip_code = request.form['zipcode']
    api_key = weather_api.get_api_key()
    data = weather_api.get_weather(zip_code, api_key)
    temp = int(data['main']['temp'])
    weather = data["weather"][0]["main"]
    location = data["name"]
    restaurant = yelp_api.businesses(zip_code)
    return render_template('results.html', location = location, temp = temp, weather = weather, restaurants = restaurant)


if __name__ == '__main__':
    app.run()

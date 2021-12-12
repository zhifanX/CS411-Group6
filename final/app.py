from flask import Flask, render_template, request, session, url_for, redirect
from util import weather_api
from util import yelp_api
from util import ranking
from authlib.integrations.flask_client import OAuth
from util import google

app = Flask(__name__)

google_secret_key = google.get_secret_key()
google_client_id = google.get_client_id()
google_client_secret = google.get_client_secret()

app.secret_key = google_secret_key

oauth = OAuth(app)
google = oauth.register(
    name='google',
    client_id= google_client_id,
    client_secret= google_client_secret,
    access_token_url = 'https://accounts.google.com/o/oauth2/token',
    access_token_params=None,
    authorize_url='https://accounts.google.com/o/oauth2/auth',
    authorize_params=None,
    api_base_url='https://www.googleapis.com/oauth2/v1/',
    client_kwargs={'scope': 'openid email profile'},
)

@app.route('/')
def login():
    google = oauth.create_client('google')
    redirect_uri = url_for('authorize', _external=True)
    return google.authorize_redirect(redirect_uri)

@app.route('/authorize')
def authorize():
    google = oauth.create_client('google')
    token = google.authorize_access_token()
    resp = google.get('userinfo')
    user_info = resp.json()
    session['email'] = user_info['email']
    return redirect('/home')

@app.route('/home')
def weather_search():
    return render_template('home.html')

@app.route('/results', methods = ['POST'])
def results():
    names = []
    links = []
    rating = []
    marker = []
    zip_code = request.form['zipcode']
    radius = request.form['radius']
    api_key = weather_api.get_api_key()
    data = weather_api.get_weather(zip_code, api_key)
    temp = int(data['main']['temp'])
    weather = data["weather"][0]["main"]
    location = data["name"]
    restaurant = ranking.sort_by_ranking(ranking.sort_by_weather(temp, weather, yelp_api.businesses(radius, zip_code)))
    for biz in restaurant:
        print(biz['categories'])
        names.append(biz["name"])
        links.append(biz["url"])
        rating.append(biz['rating'])
        marker.append(biz['coordinates'])
        lat_map = biz['coordinates']['latitude']
        long_map = biz['coordinates']['longitude']
    return render_template('results.html', location = location, temp = temp, weather = weather, restaurants = names, links = links, rating = rating, long_map = long_map, lat_map = lat_map, marker = marker)

@app.route('/logout')
def logout():
    for key in list(session.keys()):
        session.pop(key)
    return redirect('/')

if __name__ == '__main__':
    app.run()

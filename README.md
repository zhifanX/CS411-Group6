# CS411-Group6

# Overview:

This project is about creating a Flask app that recommend restaurants according to location and weather.

# Prerequisites:

Python version 3.8

# Requirements:

Click==7.0

Flask==1.1.1 (pip install flask)

itsdangerous==1.1.0

Jinja2==2.11.1

MarkupSafe==1.1.1

Werkzeug==1.0.0

# OAuth

Authlib Flask (pip install Authlib Flask)

Requests (pip install requests)

Google credentials (AOuth client Id from console.cloud.google.com)

# API Keys
OpenWeatherMap API:
https://openweathermap.org/api - Current Weather Data

Yelp Fusion API:
https://www.yelp.com/developers/documentation/v3/business_search -  Business Endpoints

Google Map API:
https://maps.googleapis.com

- Enter key information under respective title in config.ini file. 
- For Google Map API, insert API key and link into results.html file under the script section labeled <script asyn defer src = [add link here]>

# Running application
- Install pip through instructions found here: https://pip.pypa.io/en/stable/installation/
- Install virual environment through instructions found here: https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/
- Install package requirements:
    - Necessary packages can be found on top of app.py file and python files within util
- Install flask through instructions found here: https://flask.palletsprojects.com/en/2.0.x/installation/
- Clone the following repo into your virtual environment
- Enter into file labeled "final"
    - Run app by typing in 
    ```
    python app.py
    ```
  

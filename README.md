# CS411-Group6
# Final Project Demo
[Click here](https://drive.google.com/file/d/1Pk0GHcVywG__QOkisT5ko84yzXEvulIl/view?usp=sharing)
# Overview:

This project is about creating a Flask app that recommends restaurants according to location and weather. Based on temperature and forecast, our top secret algorithm helps rank and provide restaurants that would most fit your palet in the appropriate weather. Restaurants can then be saved for future visits.

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

Authlib Flask 
```
pip install Authlib Flask
```
Requests 
```
pip install requests
```

Google credentials (AOuth client Id from https://console.cloud.google.com)

# API Keys
OpenWeatherMap API:
https://openweathermap.org/api - Current Weather Data

Yelp Fusion API:
https://www.yelp.com/developers/documentation/v3/business_search -  Business Endpoints

Google Map API:
https://maps.googleapis.com

- Enter key information under respective title in config.ini file. 
- For Google Map API, insert API key and link into results.html file under the script section labeled 
```
<script asyn defer src = [add link here]>
```

# Running application
- Install pip through instructions found here: https://pip.pypa.io/en/stable/installation/
- Install virual environment through instructions found here: https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/
- Install package requirements:
    - Necessary packages can be found on top of app.py file and python files within util
```
pip install authlib
```
- Install flask through instructions found here: https://flask.palletsprojects.com/en/2.0.x/installation/
``` 
pip install flask
```
- Clone the following repo into your virtual environment
- Enter into file labeled "final"
    - Run app by typing in 
```
python app.py
```
  

import requests
import configparser


zip_code = 0
radius = 0

def get_api_key():
    config = configparser.ConfigParser()
    config.read('config.ini')
    return config['yelp']['yelp_api']


def businesses(rad, zip):
    global zip_code
    global PARAMETERS
    global radius
    zip_code = zip
    list = []
    PARAMETERS['location'] = zip_code
    PARAMETERS['radius'] = rad
    data = requests.get(url = ENDPOINT, params = PARAMETERS, headers = HEADERS).json()
    for businesses in data['businesses']:
        list.append(businesses)
    return list


ENDPOINT = 'https://api.yelp.com/v3/businesses/search'
HEADERS = {'Authorization': 'bearer %s' % get_api_key()}
PARAMETERS = {'term': 'food',
              'limit': 10,
              'radius': 10000,
              'location': "%d" % zip_code}

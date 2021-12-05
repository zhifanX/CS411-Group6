import requests
import configparser


global zip_code

zip_code = 0

def get_api_key():
    config = configparser.ConfigParser()
    config.read('config.ini')
    return config['yelp']['yelp_api']


def businesses(zip):
    global zip_code
    print(zip_code)
    zip_code = zip
    print(zip_code)
    list = []
    data = response.json()
    for businesses in data['businesses']:
        list.append(businesses['name'])
    return list


ENDPOINT = 'https://api.yelp.com/v3/businesses/search'
HEADERS = {'Authorization': 'bearer %s' % get_api_key()}
PARAMETERS = {'term': 'coffee',
              'limit': 10,
              'radius': 10000,
              'location': zip_code}

print(PARAMETERS['location'])

response = requests.get(url = ENDPOINT, params = PARAMETERS, headers = HEADERS)

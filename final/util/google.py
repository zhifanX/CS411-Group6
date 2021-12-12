import requests
import configparser


def get_secret_key():
    config = configparser.ConfigParser()
    config.read('config.ini')
    return config['secret_key']['secret_key']

def get_client_id():
    config = configparser.ConfigParser()
    config.read('config.ini')
    return config['client_id']['client_id']


def get_client_secret():
    config = configparser.ConfigParser()
    config.read('config.ini')
    return config['client_secret']['client_secret']

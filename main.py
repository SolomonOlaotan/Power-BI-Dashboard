# load necessary libraries
import requests #to connect to API
import pandas as pd # for data transformation
import configparser # to create my configuration
from sqlalchemy import create_engine # for communication with postgres


# create configparser instance
config = configparser.configParser()


#create openweather credential
api_key = config['openweather']['api_key']
lat = config['openweather']['lat']
lon = config['openweather']['lon']
city_id = config['openweather']['city_id']
city_name = 'kaduna'


#start postgres engine
postgres_config = config['postgres']
engine = create_engine("postgressql://username:password@host/database")


#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
import requests
from flight_search import FlightSearch
from data_manager import DataManager
from pprint import pprint

data_manager = DataManager()
sheet_data = data_manager.get_sheet_data()

for flight in sheet_data:
    if flight['iataCode'] == '':
        FlightSearch(flight).update_iataCode()

data_manager.iataCode_sheet_update(sheet_data)







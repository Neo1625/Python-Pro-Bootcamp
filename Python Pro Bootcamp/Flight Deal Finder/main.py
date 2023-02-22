#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from flight_search import FlightSearch
from data_manager import DataManager
from flight_data import FlightData
import datetime
from pprint import pprint

data_manager = DataManager()
sheet_data = data_manager.get_sheet_data()

for flight in sheet_data:
    if flight['iataCode'] == '':
        FlightSearch(flight).update_iataCode()

data_manager.iataCode_sheet_update(sheet_data)

for city in sheet_data:
    destination = city['iataCode']
    flight_data = FlightData(destination)
    print(f"{destination}: {flight_data.flight_price()}")







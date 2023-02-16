# This class is responsible for talking to the Flight Search API.
import requests

class FlightSearch:
    def __init__(self, flight):
        self.flight = flight

    def update_iataCode(self):
        search_endpoint = "https://api.tequila.kiwi.com/locations/query"
        header = {"apikey": "c_Dc_td_4P0St3Q4p53YvvMrZk0nRznR"}
        query = {
            "term": self.flight['city'],
        }
        response = requests.get(url=search_endpoint, headers=header, params=query)
        response.raise_for_status()
        data = response.json()
        locations = data['locations']
        city = locations[0]['code']
        self.flight['iataCode'] = city


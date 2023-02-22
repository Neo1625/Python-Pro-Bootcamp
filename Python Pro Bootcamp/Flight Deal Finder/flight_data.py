#This class is responsible for structuring the flight data.
import requests
import datetime

FLIGHT_SEARCH_ENDPOINT = "https://api.tequila.kiwi.com/v2/search"
API_KEY = "c_Dc_td_4P0St3Q4p53YvvMrZk0nRznR"

class FlightData:
    def __init__(self, destination_city):
        self.destination_city = destination_city

    def flight_price(self):
        header = {"apikey": API_KEY}
        payload = {
            "fly_from": "LON",
            "fly_to": self.destination_city,
            "date_from": self.date_from_to_calc(1),
            "date_to": self.date_from_to_calc(6*30),
            "one_for_city": 1,
            "flight_type": "round",
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "curr": "GBP"
        }
        response = requests.get(url=FLIGHT_SEARCH_ENDPOINT, headers=header, params=payload)
        price = response.json()['data'][0]['price']
        return price





    def date_from_to_calc(self, num_of_days):
        now = datetime.datetime.now()
        tomorrow = now + datetime.timedelta(days=num_of_days)
        return tomorrow.strftime("%d/%m/%Y")


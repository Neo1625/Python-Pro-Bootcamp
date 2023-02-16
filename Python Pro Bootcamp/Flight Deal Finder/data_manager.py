#This class is responsible for talking to the Google Sheet.
import requests

URL = "https://api.sheety.co/34a2c87e9b37d46066b80a08620c3f77/myOwnCopyOfFlightDeals/prices"

class DataManager:

    def __init__(self):
        self.data = {}

    def get_sheet_data(self):
        response = requests.get(url=URL)
        response.raise_for_status()
        self.data = response.json()['prices']
        return self.data

    def iataCode_sheet_update(self, updated_data):
        for flight in updated_data:
            payload = {
                "price": {
                    "iataCode": flight['iataCode']
                }
            }
            response = requests.put(url=f"{URL}/{flight['id']}", json=payload)
            if response.status_code == 200:
                print(f"IATACODE at row {flight['id']} successfully updated!")
            else:
                print(f"Error updating IATACODE at row {flight['id']}.")




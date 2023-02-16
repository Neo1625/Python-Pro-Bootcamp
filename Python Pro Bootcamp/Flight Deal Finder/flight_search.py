# This class is responsible for talking to the Flight Search API.
class FlightSearch:
    def __init__(self, flight):
        self.flight = flight

    def update_iataCode(self):
        self.flight['iataCode'] = "TESTING"


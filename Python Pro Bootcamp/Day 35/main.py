import requests

OWN_Endpoint = "https://api.openweathermap.org/data/2.5/onecall"
#api_key = "eb15d6281ebe7a905f8b742bb9a32e07"
api_key = "b1d43d24a247821ce991a532d13c7355"

params = {
    "lat": 29.950226,
    "long": -96.257187,
    "appid": api_key
}

response = requests.get(OWN_Endpoint, params=params)
print(response.status_code)


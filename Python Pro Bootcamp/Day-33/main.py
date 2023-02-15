import requests
from datetime import datetime

#response = requests.get(url="http://api.open-notify.org/iss-now.json")
#response.raise_for_status()

#data = response.json()
#print(data)

#latitude = data['iss_position']['latitude']
#longitude = data['iss_position']['longitude']

#iss_position = (latitude, longitude)
#print(iss_position)


MY_LAT = "29.950226"
MY_LONG = "-96.257187"

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0
}

response = requests.get(url=" https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()

sunrise = data['results']['sunrise'].split("T")[1].split(":")[0]
sunset = data['results']['sunset'].split("T")[1].split(":")[0]

print(sunrise)

time_now = datetime.now()
print(time_now.hour)




import requests
import datetime

pixela_endpoint = "https://pixe.la/v1/users"

TOKEN = "erfru4vb24gojr8g0j9p"
USERNAME = "morpheus"
GRAPH_ID = "neo1625"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

#response = requests.post(url=pixela_endpoint, json=user_params)
#print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": GRAPH_ID,
    "name": "reading Graph",
    "unit": "pages",
    "type": "float",
    "color": "ajisai",
}

headers = {
    "X-USER-TOKEN": TOKEN
}

#response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
#print(response.text)

pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

today = datetime.datetime(year=2022, month=12, day=15)

request_body = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "25",
}

#response = requests.post(url=pixel_endpoint, headers=headers, json=request_body)
#print(response.text)

update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{request_body['date']}"

new_data = {
    "quantity": "12",
}

#response = requests.put(url=update_endpoint, headers=headers, json=new_data)
#print(response.text)

delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{request_body['date']}"
response = requests.delete(url=delete_endpoint, headers=headers)
print(response.text)


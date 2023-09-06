import requests
from datetime import datetime

# Register a user account and then create a pixela graph to work with

PIXELA_ENDPOINT = "https://pixe.la/v1/users"
user_params = {
    "token": 'thisissecret',
    "username": 'yakhshi94',
    "agreeTermsOfService": 'yes',
    "notMinor": 'yes'
    }
# response = requests.post(PIXELA_ENDPOINT, json=user_params)
USER_NAME = "yakhshi94"
GRAPH_ENDPOINT = f"{PIXELA_ENDPOINT}/{USER_NAME}/graphs"
HEADER = {'X-USER-TOKEN': 'thisissecret'}
GRAPH_ID = 'graph1'
graph_config = {
    "id": GRAPH_ID,
    "name": 'Cycling graph',
    "unit": 'km',
    "type": 'float',
    "color": 'sora'
}
# response = requests.post(url=GRAPH_ENDPOINT, json=graph_config, headers=HEADER)

PIXEL_CREATION_ENDPOINT = f"{GRAPH_ENDPOINT}/{GRAPH_ID}"

today = datetime(year=2023, month=7, day=23)

record_params = {
    'date': today.strftime("%Y%m%d"),
    'quantity': '15.5',
}

# response = requests.post(url=PIXEL_CREATION_ENDPOINT, json=record_params, headers=HEADER)
# print(response.text)

PIXEL_UPDATE_ENDPOINT = PIXEL_CREATION_ENDPOINT

update_graph = {
    "name": "Cycling graph",
    "unit": "km",
    "color": "shibafu",
    "date": today.strftime("%Y%m%d"),
    "quantity": "10"
}

# response = requests.put(url=PIXEL_UPDATE_ENDPOINT, json=update_graph, headers=HEADER)
# print(response)

PIXEL_DELETE_ENDPOINT = f"{PIXEL_CREATION_ENDPOINT}/20230723"
response = requests.delete(url=PIXEL_DELETE_ENDPOINT, headers=HEADER)
print(response)
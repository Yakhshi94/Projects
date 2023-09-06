import requests

SHEETY_ENDPOINT = 'https://api.sheety.co/13b071e8472f7111e532dec852e62b1c/myFlightDeal/prices'


class DataManager:
    def __init__(self):
        self.destination_data = {}

    def get_destination_data(self):
        response = requests.get(SHEETY_ENDPOINT).json()
        self.destination_data = response['prices']
        return self.destination_data

    def update_price_data(self, object_id, data):
        response = requests.put(f"{SHEETY_ENDPOINT}/{object_id}", json=data)

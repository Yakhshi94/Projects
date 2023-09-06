import requests
from datetime import datetime, timedelta
from pprint import pprint
from flight_search import FlightSearch
from data_manager import DataManager
from flight_search import FlightSearch

ORIGIN_CITY_IATA = "LON"

manager = DataManager()
search = FlightSearch()
data = manager.get_destination_data()
sheet_data = data

for row in sheet_data:
    if row['iataCode'] == '':
        iatacode = search.get_destination_code(row['city'])
        row['iataCode'] = iatacode
        new_data = {
            'price': {
                'iataCode': row['iataCode'],
            }
        }
        manager.update_price_data(object_id=row['id'], data=new_data)

tomorrow = datetime.now() + timedelta(days=1)
six_month_from_today = datetime.now() + timedelta(days=(6 * 30))

for destination in sheet_data:
    flight = search.check_flights(
        ORIGIN_CITY_IATA,
        destination["iataCode"],
        from_time=tomorrow,
        to_time=six_month_from_today
    )
    if flight.destination_city == destination['city']:
        if flight.price <= destination['lowestPrice']:
            print(f"Only ${flight.price} to fly from {ORIGIN_CITY_IATA} to {destination['iataCode']}")

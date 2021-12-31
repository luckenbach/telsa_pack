from teslapy import Tesla
from st2client.client import Client
import json

def get_cache():
    client = Client()
    secret = client.keys.get_by_name(name='tesla_pack_token', decrypt=True).value
    if secret:
        return json.loads(secret)
    else:
        return {}

def get_context(user):
    with Tesla(user, cache_loader=get_cache) as tesla:
        return tesla

def get_car(car_name, t):
    if car_name is None:
        return t.vehicle_list().pop
    else:
        return next(item for item in t.vehicle_list() if item["display_name"].lower() == car_name.lower())



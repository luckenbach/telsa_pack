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
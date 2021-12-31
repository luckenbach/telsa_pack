from teslapy import Tesla
from st2 import Client


def get_cache():
    client = Client()
    secret = client.keys.get_by_name(name='tesla_pack_token', decrypt=True).value
    if secret:
        return secret
    else:
        return None

def get_context(user):
    with Tesla(user, cache_loader=get_cache()) as tesla:
        return tesla

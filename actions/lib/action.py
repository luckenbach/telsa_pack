import teslapy
from teslapy import Tesla
from st2common.runners.base_action import Action
from st2client.client import Client
import json


class BaseAction(Action):
    def __init__(self, config, car_name=None):
        super(BaseAction, self).__init__(config)
        self.client = Client()
        self.user = config.get('tesla_pack_user', None)
        self.car = None

        # This is how we get the token cache out of the kv store
        def t_loader():
            return json.loads(self.client.keys.get_by_name(name='tesla_pack_token', decrypt=True).value)

        # This is how we put it back should it get refresh
        def t_dumper(token):
            new_t = self.client.keys.get_by_name(name='tesla_pack_token', decrypt=True)
            new_t.value = json.dumps(token)
            self.client.keys.update(new_t)

        self.t = Tesla(self.user, cache_loader=t_loader, cache_dumper=t_dumper)

    def _run(self, *args, **kwargs):
        raise NotImplementedError

    def run(self, *args, **kwargs):
        car_n = kwargs.get('car_name', None)
        if car_n is None:
            self.car = self.t.vehicle_list().pop()
        else:
            self.car = next(item for item in self.t.vehicle_list() if item["display_name"].lower() == car_n.lower())
            if self.car:
                pass
            else:
                raise Exception
        try:
            return True, self._run(*args, **kwargs)
        except teslapy.HTTPError:
            return False, 'HTTP error when dealing with Tesla API'

from teslapy import Tesla
from st2common.runners.base_action import Action
from st2client.client import Client
import json

class BaseAction(Action):
    def __init__(self, config, car_name=None):
        super(BaseAction, self).__init__(config)
        self.client = Client()
        self.user = config.get('tesla_pack_user', None)
        t_loader = lambda: json.loads(self.client.keys.get_by_name(name='tesla_pack_token', decrypt=True).value)
        self.t = Tesla(self.user, cache_loader=t_loader)

    def _run(self, *args, **kwargs):
        raise NotImplementedError

    def run(self, *args, **kwargs):
        car_n = kwargs.get('car_name', None)
        if car_n is None:
            self.car = self.t.vehicle_list().pop()
        else:
            self.car = next(item for item in self.t.vehicle_list() if item["display_name"].lower() == car_n.lower())
        return True, self._run(*args, **kwargs)

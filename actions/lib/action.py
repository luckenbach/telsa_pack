from teslapy import Tesla
from st2common.runners.base_action import Action
from st2client.client import Client
import json


class BaseAction(Action):
    def __init__(self, config, car_name):
        super(BaseAction, self).__init__(config)
        self.client = Client()
        self.user = config.get('tesla_pack_user', None)
        self.t = Tesla(self.user, cache_loader=json.loads(self.client.keys.get_by_name(name='tesla_pack_token',
                                                                                       decrypt=True).value))
        if car_name is None:
            self.car = self.t.vehicle_list().pop
        else:
            self.car = next(item for item in self.t.vehicle_list() if item["display_name"].lower() == car_name.lower())

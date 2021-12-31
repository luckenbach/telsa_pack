from st2common.runners.base_action import Action
from util import get_context


class ventWindows(Action):
    def run(self, car_name):
        user = self.config.get('tesla_pack_user', None)
        if user:
            t = get_context(user=user)
        else:
            return False, 'User not defined'
        if car_name:
            c = next(item for item in t.vehicle_list() if item["display_name"].lower() == car_name.lower())
        else:
            c = t.vehicle_list().pop
        if c:
            vent = c.command('WINDOW_CONTROL', command='vent', lat=0, lon=0)
            if vent:
                return True, 'Vented'
            else:
                return False, 'Failed'

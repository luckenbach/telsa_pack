from st2common.runners.base_action import Action
from util import get_context, get_car


class closeWindows(Action):
    def run(self, car_name):
        user = self.config.get('tesla_pack_user', None)
        if user:
            t = get_context(user=user)
        else:
            return False, 'User not defined'
        c = get_car(car_name, t)
        if c:
            vent = c.command('WINDOW_CONTROL', command='close', lat=0, lon=0)
            if vent:
                return True, 'Closed'
            else:
                return False, 'Failed'
        else:
            return False, 'Could not find car!'

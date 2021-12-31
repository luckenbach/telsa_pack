from st2common.runners.base_action import Action
from util import get_context, get_car
from datetime import datetime


class preconditionCar(Action):
    def run(self, car_name: str, leave_time: int):
        user = self.config.get('tesla_pack_user', None)
        if user:
            t = get_context(user)
        else:
            return False, 'User not defined'
        c = get_car(car_name, t)
        l_time = datetime.fromtimestamp(leave_time)
        # Telsa API wants minutes past midnight
        d_time = int((l_time - l_time.replace(hour=0, minute=0, second=0)).total_seconds() / 60)
        if c:
            prep = c.command('SCHEDULED_DEPARTURE', enable=True, preconditioning_enabled=True, departure_time=d_time)
            if prep:
                return True, 'preconditioning'
            else:
                return False, 'Unable to start preconditioning'
        else:
            return False, 'Could not find car!'

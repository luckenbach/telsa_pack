from st2common.runners.base_action import Action
from util import get_context, get_car


class preconditionCar(Action):
    def run(self, car_name: str, leave_time: int):
        user = self.config.get('tesla_pack_user', None)
        if user:
            t = get_context(user)
        else:
            return False, 'User not defined'
        c = get_car(car_name, t)
        # TODO: Will come back and correct this once I have the code working below :)
        leave_time = 2000
        if c:
            prep = c.command('SCHEDULED_DEPARTURE', enable=True, preconditioning_enabled=True, departure_time=leave_time)
            if prep:
                return True, 'preconditioning'
            else:
                return False, 'Unable to start preconditioning'
        else:
            return False, 'Could not find car!'

from lib.action import BaseAction
from datetime import datetime


class preconditionCar(BaseAction):
    def _run(self, *args, **kwargs):
        leave_time = kwargs.get('leave_time', None)
        if leave_time:
            l_ts = datetime.fromtimestamp(leave_time)
        else:
            return False, 'You gotta give us a time to leave boss'
        # Telsa API wants minutes past midnight
        d_time = int((l_ts - l_ts.replace(hour=0, minute=0, second=0)).total_seconds() / 60)
        prep = self.car.command('SCHEDULED_DEPARTURE', enable=True, preconditioning_enabled=True, departure_time=d_time)
        if prep:
            return True, 'preconditioning'
        else:
            return False, 'Unable to start preconditioning'

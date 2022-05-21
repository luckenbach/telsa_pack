from lib.action import BaseAction
from

class stopCharge(BaseAction):
    def _run(self, *args, **kwargs):
        try:
            charge_stop = self.car.command('STOP_CHARGE')
        except teslapy.HTTPError:
        if charge_stop:
            return True, 'Stopped'
        else:
            return False, 'Failed'

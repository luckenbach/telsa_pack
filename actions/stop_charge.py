from lib.action import BaseAction


class stopCharge(BaseAction):
    def _run(self, *args, **kwargs):
        charge_stop = self.car.command('STOP_CHARGE')
        if charge_stop:
            return True, 'Stopped'
        else:
            return False, 'Failed'

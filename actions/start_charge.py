from lib.action import BaseAction


class startCharge(BaseAction):
    def _run(self, *args, **kwargs):
        charge_start = self.car.command('START_CHARGE')
        if charge_start:
            return True, 'Started'
        else:
            return False, 'Failed'

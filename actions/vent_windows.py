from lib.action import BaseAction

class ventWindows(BaseAction):
    def _run(self, *args, **kwargs):
        vent = self.car.command('WINDOW_CONTROL', command='vent', lat=0, lon=0)
        if vent:
            return True, 'Vented'
        else:
            return False, 'Failed'

from lib.actions import BaseAction

class ventWindows(BaseAction):
    def run(self):
        c = self.car
        vent = c.command('WINDOW_CONTROL', command='vent', lat=0, lon=0)
        if vent:
            return True, 'Vented'
        else:
            return False, 'Failed'

from lib.action import BaseAction

class honkHorn(BaseAction):
    def _run(self, *args, **kwargs):
        honk = self.car.command('HONK_HORN')
        if honk:
            return True, 'Honked'
        else:
            return False, 'We did not honk'
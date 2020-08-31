import datetime


class BaseClient():
    @property
    def now(cls):
        now = datetime.datetime.utcnow()
        isostring = now.strftime('%Y-%m-%dT%H:%M:%S.{0}Z')
        return isostring.format(int(round(now.microsecond/1000.0)))

    @property
    def report(self):
        raise NotImplementedError()

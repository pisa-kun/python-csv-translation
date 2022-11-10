import datetime

t = datetime.datetime.now()
print(t)
print(t.isoformat())

jst2utc = datetime.timedelta(hours=-9)
print(t + jst2utc)
print(datetime.datetime.utcnow())

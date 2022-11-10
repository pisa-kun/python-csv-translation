import datetime

t = datetime.datetime.now()
print(t)
print(t.isoformat())

jst2utc = datetime.timedelta(hours=-9)
print(t + jst2utc)
print(datetime.datetime.utcnow())

timestr = "2022-11-11 04:18:08.496290"
print(datetime.datetime.strptime(timestr, "%Y-%m-%d %H:%M:%S.%f"))
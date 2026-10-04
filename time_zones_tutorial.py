import datetime
import pytz

t_day = datetime.datetime(2026, 10, 4, 12, 30, 45,tzinfo = pytz.UTC)
print(t_day)

t_now = datetime.datetime.now(tz=pytz.UTC)
print(t_now)

dt_mu = t_now.astimezone(pytz.timezone('America/New_York'))

print(dt_mu)


for tz in pytz.all_timezones:
    print(tz)
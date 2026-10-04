import datetime

t = datetime.date(2026,10,4)
print(t)

tday = datetime.date.today()
tdelta = datetime.timedelta(days=7)
print(tday)
print(tday.weekday())
print(tday.isoweekday())
print(tday + tdelta)

t_date = datetime.time(16,55,34,34444)
print(t_date)
print(t_date.hour)
print(t_date.minute)
print(t_date.second)
print(t_date.microsecond)

dt_today = datetime.datetime.today()
dt_now = datetime.datetime.now()
dt_utcnow = datetime.datetime.utcnow()
print(dt_today)
print(dt_now)
print(dt_utcnow)

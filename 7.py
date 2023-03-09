import datetime as dat
today = dat.date.today()
yesterday = today - dat.timedelta(days = 1)
tomorrow = today + dat.timedelta(days = 1)
print(today)
print(yesterday)
print(tomorrow)
import datetime as dat
def foo(x , y):
    td = y - x
    return td.days*24*3600 + td.seconds
date1 = dat.datetime(2022,1,1,14,14,0)
date2 = dat.datetime(2022,1,1,14,15,30)
print(foo(date1 , date2))
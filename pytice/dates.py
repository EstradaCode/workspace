import datetime as time

print(time.datetime.now()) ## .month .day .year
print(time.date.today())
print(time.datetime.now().time())
print(time.datetime.now().strftime("%d-%m-%Y %H:%M:%S"))
print(time.datetime.now().strftime("%d-%B-%Y %H:%M:%S"))
print(time.datetime.now().strftime("%d-%b-%Y %H:%M:%S"))
#lo mismo para today pero con fecha
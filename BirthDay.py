import datetime as t

curDate = t.datetime.now()
birDate = t.datetime(2010, 11, 30)

# Current varaibles
curDay = curDate.day
curMon = curDate.month
curYear = curDate.year

# User Variables
birDay = birDate.day
birMon = birDate.month
birYear = birDate.year

# Month Variables
months = (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)

# logic 

if birDay > curDay and birMon >= curMon:
    dd=curDay + months[birMon] - birDay
    mm=curMon-1+12-birMon
    yr=curYear-1-birYear

elif birDay > curDay and birMon < curMon:
    dd=curDay+months[birMon]- birDay
    mm=curMon-birMon
    yr=curYear-birYear

elif birDay < curYear and birMon > curMon:
    dd=curDay - birDay
    mm=curMon+12-birMon
    yr=curYear-1-birYear

else :
     dd=curDay-birDay
     mm=curMon-birMon
     yr=curYear-birYear

print("\n\n Your age is {} Yrs {} Months and {} days\n\n".format(yr,mm,dd))




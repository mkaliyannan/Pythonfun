import datetime as t

curDate = t.datetime.now()
birDate = t.datetime(1985, 7, 17)
curDay = curDate.day
curMon = curDate.month
curYear = curDate.year
nxtYear = curDate.year
birDay = birDate.day
birMon = birDate.month
birYear = birDate.year
months = (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)

if birDay > curDay:
    curDay = curDay + months[curMon] - birDay
    curMon = curMon - 1

if birMon > curMon:
    curMon = curMon + 12 - birMon
    curYear = curYear - 1 - birYear


if birMon == curMon and birDay > curDay:
    curDay = curDay + months[curMon] - birDay
    curMon = curMon - 1

if birMon == curMon and birDay < curDay:
    curMon = curMon - birMon
    curYear = curYear - birYear
    curDay = curDay - birDay

if birDay == curDay and birMon == curMon:
    curYear = curYear - birYear
    curMon = curMon - birMon
    curDay = curDay - birDay

print("\n\nYour age is :\n\n{} Years {} Months and {} Days old.\n\n".format(
    curYear, curMon, curDay))

if curMon == curDay:
    print("\n\nHappy Birthday !\n\n\n")
'''
if birMon == curDate.month and birDay < curDate.day:
        nbd = t.datetime(nxtYear, birMon, birDay).date()
        cdy = t.datetime.now().date()
        x = nbd-cdy
        print("Your birthday will be in next {} days".format(x.days)) 

if birMon == curDate.month and birDay > curDate.day:
        nbd = t.datetime(nxtYear, birMon, birDay).date()
        cdy = t.datetime.now().date()
        x = nbd-cdy
        print("Your birthday will be in next {} days".format(x.days)) 


if birMon > curDate.month:
        nbd = t.datetime(nxtYear, birMon, birDay).date()
        cdy = t.datetime.now().date()
        x = nbd-cdy
        print("Your birthday will be in next {} days".format(x.days))  
          

if birMon < curDate.month:
        nbd = t.datetime(nxtYear+1, birMon, birDay).date()
        cdy = t.datetime.now().date()
        x = nbd-cdy
        print("Your birthday will be in next {} days".format(x.days))
'''
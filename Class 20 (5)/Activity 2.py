import random
import time

def randomtime(start, end):
    print('Printing random Date and Time between', start, 'and', end)
    randnum = random.random()
    dateformat = "%m/%d/%y"
    starttime = time.mktime(time.strptime(start, dateformat))
    endtime = time.mktime(time.strptime(end, dateformat))
    randtime = starttime + randnum * (endtime - starttime)
    randomdate = time.strftime(dateformat, time.localtime(randtime))
    return randomdate
print(randomtime('11/1/20' , '2/1/25'))
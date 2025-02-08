#Date and Time
from datetime import datetime ,date, time

x = datetime.now()
print(x)

d = date.today()
print(d)

print('The DateTime components are : (Year)',d.year,'(Month)', d.month,'(Day)' ,d.day)
# import datetime importa o objeto total
from datetime import date #importa a variavel especifica

print(date.today())

from datetime import datetime

from datetime import timedelta

print(datetime.now())
print(datetime.now().strftime("%a, %d. %B/%Y : %x %X"))
print(datetime.now().replace(datetime.now().year + 1))

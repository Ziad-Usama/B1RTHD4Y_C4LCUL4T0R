import time
from datetime import date
today = date.today()
birthday = date(today.year, 9, 20) #insert date Here (YY , MM, DD)
if birthday < today:
    birthday.replace(year=today.year +1)
days_left = abs(birthday - today)
print(str(days_left.days)+" Days Left")


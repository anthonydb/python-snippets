from datetime import date
from datetime import timedelta

today = date.today()
offset = (today.weekday() - 3) % 7
last_thursday = today - timedelta(days=(offset+14))
print(last_thursday)


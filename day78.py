
from datetime import datetime

date = datetime.strptime(input(), "%m %d %Y")
weekday = date.strftime("%A").upper()
print(weekday)

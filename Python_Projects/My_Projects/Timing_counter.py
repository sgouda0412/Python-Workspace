import datetime

# Todays Date
now = datetime.date(2020, 12, 17)

# 19th October 
start = datetime.date(2020, 10, 19)

delta = now - start
print(f"{delta.days} days have passed")

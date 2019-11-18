import datetime

today = datetime.date.today()

previous_weeks = [] # list to store previous weeks
for a in range(1,27):
    last_week = today.__add__(datetime.timedelta(days=-7))
    previous_weeks.append(last_week)
    today = last_week

for i in previous_weeks:
    print(i)
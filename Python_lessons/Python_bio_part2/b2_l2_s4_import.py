import datetime

i = input().split()
date = datetime.date(int(i[0]), int(i[1]), int(i[2]))
days = datetime.timedelta(int(input()))

print(date + days)
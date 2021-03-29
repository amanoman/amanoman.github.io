from datetime import datetime
import time

now = time.time()

print(now)
print(type(now))
loc = datetime.fromtimestamp(now).strftime("%Y/%m/%d %H:%M")
print(loc)

utc = datetime.utcfromtimestamp(now)
print(utc)
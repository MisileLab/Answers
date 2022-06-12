from datetime import timezone
import datetime

dt = datetime.datetime.now(timezone.utc).replace(tzinfo=timezone.utc)

print(dt.year)
print(dt.month)
print(dt.day)
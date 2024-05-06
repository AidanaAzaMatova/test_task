# Этот код скопирован из источника - https://www.geeksforgeeks.org/how-to-convert-datetime-to-unix-timestamp-in-python/
# импортируем модуль datetime
import datetime
# импортируем модуль time
import time

# назначенная обычная строковая дата
date_time = datetime.datetime.now()

# печатать обычную дату и время на python
print("date_time =>", date_time)

# отображение временной метки unix после преобразования
print("unix_timestamp => ",
      (time.mktime(date_time.timetuple())))
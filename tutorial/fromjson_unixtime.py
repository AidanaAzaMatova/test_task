# Этот код скопирован из источника - https://www.geeksforgeeks.org/how-to-convert-datetime-to-unix-timestamp-in-python/
# импортируем модуль datetime
import datetime
# импортируем модуль time
import time

# назначенная обычная строковая дата
date_time = datetime.datetime.now()
# Экспериментируем пишем хард - код (это очень плохо)
# Берем пример из json полученную дату в виде строки str
str_time = '2024-05-06T22:13:04+05:00'
# date_time = datetime.datetime(2024, 5, 5, 14, 10) - берем как пример
a = int(str_time[0]+str_time[1]+str_time[2]+str_time[3])
b = int(str_time[5]+str_time[6])
c = int(str_time[8]+str_time[9])
d = int(str_time[11]+str_time[12])
e = int(str_time[14]+str_time[15])
date_time = datetime.datetime(a, b, c, d, e)

# печатать обычную дату и время на python
print("date_time =>", date_time)

# отображение временной метки unix после преобразования
print("unix_timestamp => ",
      (time.mktime(date_time.timetuple())))
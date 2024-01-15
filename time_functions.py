import datetime
from datetime import timedelta

""" Доктор принимает с 9 утра до 9 вечера.
Часть времени у него занята: приемы, обед, уборка кабинета.

Требуется сформировать список свободных окон по 30 минут.
"""

"список перерывов врача"
busy = [
{'start' : '10:30',
'stop' : '10:50'
},
{'start' : '18:40',
'stop' : '18:50'
},
{'start' : '14:40',
'stop' : '15:50'
},
{'start' : '16:40',
'stop' : '17:20'
},
{'start' : '20:05',
'stop' : '20:20'
}
]

"сортируем список по ключу 'start' "
sorted_list = sorted(busy, key=lambda x: x['start'])

def find_interval(h1: int, m1 : int, h2: int, m2: int,intetval: int) -> int:
    """высчитывает количество окон(interval) между временем 1(h1 = часы, m2 = минуты) и временем 2. Возвращает количество
    окон между промежутками времени"""

    time1 = timedelta(hours=h1, minutes=m1)
    time2 = timedelta(hours=h2, minutes=m2)
    window = timedelta(minutes=intetval)
    res = (time2 - time1) // window

    return res


# задаем счетчик окон, начальное время, конечное время и длинну интервала
count_interval = 0
start_time = (9, 0)
finish_time = (21, 0)
window = 30

# переводим начальное и конечное время в более читаемый вид для подстановки в функцию
h1 = start_time[0]
m1 = start_time[1]
h2 = int(sorted_list[0]['stop'].split(':')[0])
m2 = int(sorted_list[0]['stop'].split(':')[1])

# считаем окна в первом интервале
count_interval += find_interval(h1, m2, h2, m2, window)

# считаем окна в оставшемся промежутке времени
for i in range(len(sorted_list)):
    if i < len(sorted_list):
        try:
            h1 = int(sorted_list[i]['stop'].split(':')[0])
            m1 = int(sorted_list[i]['stop'].split(':')[1])
            h2 = int(sorted_list[i+1]['start'].split(':')[0])
            m2 = int(sorted_list[i+1]['start'].split(':')[1])
            count_interval += find_interval(h1, m1, h2, m2, window)

        except Exception:
            h1 = int(sorted_list[i]['stop'].split(':')[0])
            m1 = int(sorted_list[i]['stop'].split(':')[1])
            h2 = finish_time[0]
            m2 = finish_time[1]
            count_interval += find_interval(h1, m1, h2, m2, window)


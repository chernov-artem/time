import datetime
from datetime import timedelta

""" Доктор принимает с 9 утра до 9 вечера.
Часть времени у него занята: приемы, обед, уборка кабинета.

Требуется сформировать список свободных окон по 30 минут.
"""

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
rest_list = []


def find_interval(h1: int, m1 : int, h2: int, m2: int,intetval: int):
    "высчитывает количество окон(interval) между временем 1(h1 = часы, m2 = минуты) и временем 2"

    time1 = timedelta(hours=h1, minutes=m1)
    time2 = timedelta(hours=h2, minutes=m2)
    print(time2 - time1, intetval)
    window = timedelta(minutes=intetval)

    return (time2 - time1) // window



find_interval(9, 0, 10, 30, 30)
# count_interval = 0
# start_time = (9, 0)
# finish_time = (21, 0)
#
#
# for i in busy:
#     print(i['start'], i['stop'])
#
#
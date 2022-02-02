
#1. Реализовать вывод информации о промежутке времени в зависимости от его продолжительности duration в секундах.
#Формат вывода результата:

#до минуты: <s> сек;
#до часа: <m> мин <s> сек;
#до суток: <h> час <m> мин <s> сек;
#в остальных случаях: <d> дн <h> час <m> мин <s> сек.
#Примеры/Тесты:

#duration = 53: 53 сек
#duration = 153: 2 мин 33 сек
#duration = 4153: 1 час 9 мин 13 сек
#duration = 400153: 4 дн 15 час 9 мин 13 сек
# Реализация происходит в секундах

#Я хочу чтобы пользователь прописовал мог узнать сколько(дней,лет,часов и т.д)
# в секундах, для начала я узнаю сколько в каждом кратном значение одному секунд,
# зачем я хочу сделать если значение одной переменной становится кратно другой то записывается переменная на порядок больше)

duration = int(input('Specify the time you are interested in in seconds: '))
#if duration < 60:
    #print(duration, ("секунд."))
#else: #duration >= one_minute:
    #present_time_year = duration // (60 * 60 * 24*365)
    #present_time_month = duration // (60 * 60 * 24*30)
    #present_time_week = duration // (60 * 60 * 24*7)
   # present_time_day = duration // (60 * 60 * 24)
    #present_time_hour = (duration - present_time_day * (60 * 60 * 24)) // (60 * 60)
   # present_time_minute = (duration - present_time_day * (60 * 60 * 24) - present_time_hour * (60 * 60)) // 60
   # present_time_second = duration - present_time_day * (60 * 60 * 24) - present_time_hour * (60 * 60) - present_time_minute * 60
   # print(int(present_time_year), "year", int(present_time_month), "month", int(present_time_week), "week", int(present_time_day), "day", int(present_time_hour), "hour", int(present_time_minute), "minute", int(present_time_second), "second" )
one_second = 1
one_minute = 60
one_hour = 3600
one_day = 86400
one_week = 604800
one_month = 2629743
one_year = 31556926
if duration<one_minute:
    print(duration, ("second."))
elif one_hour >= duration:
    present_time_minute = duration // one_minute
    present_time_second = duration % one_minute
    print(int(present_time_minute), "minute", int(present_time_second), "second" )
elif one_day >= duration:
    present_time_hour = duration // one_hour
    duration = duration % one_hour
    present_time_minute = duration // one_minute
    present_time_second = duration % one_minute
    print(int(present_time_hour), "hour", int(present_time_minute), "minute", int(present_time_second), "second" )
elif one_week >= duration:
    present_time_day = duration // one_day
    duration = duration % one_day
    present_time_hour = duration // one_hour
    duration = duration % one_hour
    present_time_minute = duration // one_minute
    present_time_second = duration % one_minute
    print(int(present_time_day), "day", int(present_time_hour), "hour", int(present_time_minute), "minute", int(present_time_second), "second" )
elif one_month >= duration:
    present_time_week = duration // one_week
    duration = duration % one_week
    present_time_day = duration // one_day
    duration = duration % one_day
    present_time_hour = duration // one_hour
    duration = duration % one_hour
    present_time_minute = duration // one_minute
    present_time_second = duration % one_minute
    print(int(present_time_week), "week", int(present_time_day), "day", int(present_time_hour), "hour", int(present_time_minute), "minute", int(present_time_second), "second" )
elif one_year >= duration:
    present_time_month = duration // one_month
    duration = duration % one_month
    present_time_week = duration // one_week
    duration = duration % one_week
    present_time_day = duration // one_day
    duration = duration % one_day
    present_time_hour = duration // one_hour
    duration = duration % one_hour
    present_time_minute = duration // one_minute
    present_time_second = duration % one_minute
    print(int(present_time_month), "month", int(present_time_week), "week",int(present_time_day), "day", int(present_time_hour), "hour", int(present_time_minute), "minute",int(present_time_second), "second")
elif one_year <= duration:
    present_time_year = duration // one_year
    duration = duration % one_year 
    present_time_month = duration // one_month
    duration = duration % one_month
    present_time_week = duration // one_week
    duration = duration % one_week
    present_time_day = duration // one_day
    duration = duration % one_day
    present_time_hour = duration // one_hour
    duration = duration % one_hour
    present_time_minute = duration // one_minute
    present_time_second = duration % one_minute
    print(int(present_time_year), "year", int(present_time_month), "month", int(present_time_week), "week", int(present_time_day), "day", int(present_time_hour), "hour", int(present_time_minute), "minute", int(present_time_second), "second" )

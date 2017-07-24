"""
Для обоих версий 2.х и 3.х

timer(spam, 1, 2, a=3, b=4, _replays=1000) вызывает и измеряет время
работы функции spam(1, 2, a=3) _replays раз, и возвращает общее время,
затраченное на все вызовы, с результатом вызова испытуемой функции;

best(spam, 1, 2, a=3, b=4, _replays=50) многократно вызывает функцию timer,
чтобы исключить влияние флуктуаций в нагрузке на систему, и возвращает
лучший результат из серии по _replays испытаниям.
"""

import sys
import time

if sys.platform[:3] == 'win':
    # В Windows использовать time.clock
    time_function = time.clock
else:
    # На некоторых платформах Unix дает лучшее разрешение
    time_function = time.time


def trace(*args):
    # Заглушка: вывод аргументов
    pass


def timer(func, *pargs, **kargs):
    # Полученное число повторов или значение по умолчанию
    _replays = kargs.pop('_replays', 1000)
    trace(func, pargs, kargs, _replays)
    # Вызов range вынесен за пределы цикла for для версии 2.6
    replays_list = range(_replays)
    start = time_function()
    for i in replays_list:
        ret = func(*pargs, **kargs)
    elapsed = time_function() - start
    return (elapsed, ret)


def best(func, *pargs, **kargs):
    _replays = kargs.pop('_replays', 50)
    best = 2 ** 32
    for i in range(_replays):
        (time, ret) = timer(func, *pargs, _replays=1, **kargs)
        if time < best:
            best = time
    return (best, ret)

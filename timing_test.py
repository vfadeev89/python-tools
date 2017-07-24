"""
Для версии 3.х

timer(spam, 1, 2, a=3, b=4, _replays=1000) вызывает и измеряет время
работы функции spam(1, 2, a=3) _replays раз, и возвращает общее время,
затраченное на все вызовы, с результатом вызова испытуемой функции;

best(spam, 1, 2, a=3, b=4, _replays=50) многократно вызывает функцию timer,
чтобы исключить влияние флуктуаций в нагрузке на систему, и возвращает
лучший результат из серии по _replays испытаниям.
"""

import sys
import time

# В Windows использовать time.clock
# На некоторых платформах Unix дает лучшее разрешение
time_function = time.clock if sys.platform == 'win32' else time.time


# Заглушка: вывод аргументов
def trace(*args):
    pass


def timer(func, *pargs, _replays=1000, **kargs):
    """
    Расчитывает общее время выполнения функция _replays кол-во раз
    :param func: 
    :param pargs: 
    :param _replays: 
    :param kargs: 
    :return elapsed: Время, за которое выполнилось _replays кол-во функций
    :return ret: Результат выполнения функции
    """
    trace(func, pargs, kargs, _replays)
    start = time_function()
    for i in range(_replays):
        ret = func(*pargs, **kargs)
    elapsed = time_function() - start
    return elapsed, ret


def best(func, *pargs, _replays=50, **kargs):
    """
    Расчитывает лучшее время выполнения функции за _replays кол-во раз
    :param func: 
    :param pargs: 
    :param _replays: 
    :param kargs: 
    :return best: Лучшее время выполнения функции за _replays кол-во раз
    :return ret: Результат выполнения функции
    """
    best = 2 ** 32
    for i in range(_replays):
        t, ret = timer(func, *pargs, _replays=1, **kargs)
        if t < best:
            best = t
    return best, ret

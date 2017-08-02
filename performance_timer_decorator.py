import time


def performance_timer(label='', trace=True):
    class PerformanceTimer:
        def __init__(self, func):
            self.func = func
            self.alltime = 0

        def __call__(self, *args, **kwargs):
            start = time.clock()
            result = self.func(*args, **kwargs)
            elapsed = time.clock() - start
            self.alltime += elapsed
            if trace:
                format = '{0} {1}: elapsed: {2:f}, self.alltime: {3:f}'
                values = (label, self.func.__name__, elapsed, self.alltime)
                print(format.format(*values))
            return result

    return PerformanceTimer


@performance_timer(label='[CCC]==>')
def list_comp(n):
    return [x * 2 for x in range(n)]


@performance_timer(trace=True, label='[MMM]==>')
def map_call(n):
    return map(lambda x: x * 2, range(n))


for func in (list_comp, map_call):
    result = list(func(5))
    func(500000)
    func(5000000)
    func(10000000)
    print('result:', result)
    print('allTime = {:f}'.format(func.alltime))  # Общее время всех вызовов map_call

print()
print('map / comp = {:f}'.format(map_call.alltime / list_comp.alltime))

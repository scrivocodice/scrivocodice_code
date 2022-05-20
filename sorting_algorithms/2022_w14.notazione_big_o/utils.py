import time

def timeit(method):
    def timed(*args, **kwargs):
        ts = time.time()
        result = method(*args, **kwargs)
        te = time.time()
        if 'log_time' in kwargs:
            name = kwargs.get('log_name', method.__name__.upper())
            kwargs['log_time'][name] = int((te - ts) * 1000)
        else:
            print('%r  %2.22f ms' % (method.__name__, (te - ts) * 1000))
        return result
    return timed


def get_matrice(righe, colonne):
    matrice = []
    for riga in range(righe):
        matrice.append([x for x in range(colonne)])
    return matrice

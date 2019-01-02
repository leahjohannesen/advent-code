import time

def timeit(f):
    def timed(*args, **kwargs):
        start = time.time()
        result = f(*args, **kwargs)
        end = time.time()

        print 'Ran {}, took {} seconds'.format(f.__name__, end - start)
        return result
    return timed

from collections import Counter
from itertools import chain, combinations, combinations_with_replacement, compress
from functools import reduce, cache, cached_property, cmp_to_key, lru_cache
import threading
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
from multiprocessing import Process, cpu_count, freeze_support
from collections import Counter, ChainMap, defaultdict, deque, UserDict, UserList, UserString, OrderedDict

def decorator(func):
    def wrapper(*args, **kwargs):
        print("function before calling...")
        result = func(*args, **kwargs)
        print(result)
        print("function after calling...")
        return result
    return wrapper

@decorator
def add(x, y):
    return x + y


add(4, 5)  # Call the function directly, no need for print



l = [1, 2, 3, 4]
x = Counter(l)
print(x)

print("Hello Programming....")

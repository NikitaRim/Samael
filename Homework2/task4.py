"""
Write a function that accepts another function as an argument. Then it
should return such a function, so the every call to initial one
should be cached.


def func(a, b):
    return (a ** b) ** 2


cache_func = cache(func)

some = 100, 200

val_1 = cache_func(*some)
val_2 = cache_func(*some)

assert val_1 is val_2

"""
from functools import lru_cache
from collections import Callable


def cache(func: Callable) -> Callable:
    def cache(func: Callable) -> Callable:
        cache = {}

        def wrapper(*args, **kwargs):
            if not cache.get(args):
                func_result = func(*args, **kwargs)
                cache[args] = func_result
                return func_result
            else:
                return cache[args]

        return wrapper

    def cache_lru(func: Callable) -> Callable:
        return lru_cache(func)
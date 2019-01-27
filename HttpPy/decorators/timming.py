# Python
from contextlib import wraps
from time import time
# Modules
from ..Logger import log_accent


def timming(fn):
    @wraps(fn)
    def wrapper():
        start_time = time()
        fn()
        end_time = time()
        elapsed_time = end_time - start_time
        log_accent("\nRequests made in: {} s".format(elapsed_time))
    return wrapper

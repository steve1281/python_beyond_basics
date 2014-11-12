__author__ = 'steve1281'
from functools import wraps

def check_non_negative(index):
    def validator(f):
        @wraps(f)
        def wrap(*args):
            if args[index] < 0:
                raise ValueError(
                    'Argument {} must be non-negative.'.format(index)
                )
            return f(*args)
        return wrap
    return validator

@check_non_negative(1)
def create_list(value,size):
    "takes value and replicates it in a list size number of times."
    return[value] * size




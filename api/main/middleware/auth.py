from functools import wraps

def authenticate(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        # check auth here
        print('this is middleware')
        return func(*args, **kwargs)
    return wrapper